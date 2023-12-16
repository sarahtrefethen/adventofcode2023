'''
# PART 1

## Input
    .|...\....
    |.-.\.....
    .....|-...
    ........|.
    ..........
    .........\
    ..../.\\..
    .-.-/..|..
    .|....-|.\
    ..//.|....

## Description
the grid above shows mirrors. The light enters at the upper left corner from the left,
and continues in the same direction unless it hits a line. \ an / turn the beam 90 degrees,
while - and | split the beam at 90 degree angles if they are hit the long way. How
many squares of the grid will the beam of light energize? 

## approach
This is very similar to a previous day, where we follow a path based on the characters
in the grid. The only additional element is a queue to keep track of diverging paths 
when the beam splits.
'''

with open("D16.txt","r") as file:
    input = file.read().splitlines()

TOP = 'top'
BOTTOM = 'bottom'
LEFT = 'left'
RIGHT = 'right'

for r in range(len(input)):
    print (f'[{r}] {input[r]}')

row_count = len(input)
col_count = len(input[0])

# helper functions for moving around the grid
def go_left(r, c, entry):
    if c != 0:
        return (r, c-1, RIGHT)
    return (r,c,entry)
def go_right(r, c,entry):
    if c != col_count-1:
        return (r, c+1, LEFT)
    return (r,c,entry)
def go_up(r,c,entry):
    if r != 0:
        return (r-1, c, BOTTOM)
    return (r,c,entry)
def go_down(r,c,entry):
    if r != row_count-1:
        return (r+1, c, TOP)
    return (r,c,entry)


def part1():
    # format will be (r,c,entry)
    visited = set()

    # store branches to come back to later
    queue = []

    # start in the upper left corner, 
    # coming in from the left
    r=0
    c=0
    entry=LEFT

    #follow the path
    while (r,c,entry) not in visited or len(queue) > 0:
        if (r,c,entry) in visited:
            (r,c,entry) = queue.pop()
            if (r,c,entry) in visited:
                continue

        visited.add((r,c,entry))

        match input[r][c]:
            case '|':
                if entry == LEFT or RIGHT:
                    previous=(r,c,entry)
                    (r,c,entry) = go_up(r,c,entry)
                    queue.append(go_down(*previous))
                elif entry == BOTTOM:
                    (r,c,entry) = go_up(r,c,entry)
                elif entry == TOP:
                    (r,c,entry) = go_down(r,c,entry)
            case '-':
                if entry == TOP or BOTTOM:
                    previous=(r,c,entry)
                    (r,c,entry) = go_left(r,c,entry)
                    queue.append(go_right(*previous))
                elif entry == LEFT:
                    (r,c,entry) = go_right(r,c,entry)
                elif entry == RIGHT:
                    (r,c,entry) = go_left(r,c,entry)
            case '\\':
                if entry == LEFT:
                    (r,c,entry) = go_down(r,c,entry)
                elif entry == BOTTOM:
                    (r,c,entry) = go_left(r,c,entry)
                elif entry == TOP:
                    (r,c,entry) = go_right(r,c,entry)
                elif entry == RIGHT:
                    (r,c,entry) = go_up(r,c,entry)
            case '/':
                if entry == LEFT:
                    (r,c,entry) = go_up(r,c,entry)
                elif entry == BOTTOM:
                    (r,c,entry) = go_right(r,c,entry)
                elif entry == TOP:
                    (r,c,entry) = go_left(r,c,entry)
                elif entry == RIGHT:
                    (r,c,entry) = go_down(r,c,entry)
            case '.':
                if entry == LEFT:
                    (r,c,entry) = go_right(r,c,entry)
                elif entry == BOTTOM:
                    (r,c,entry) = go_up(r,c,entry)
                elif entry == TOP:
                    (r,c,entry) = go_down(r,c,entry)
                elif entry == RIGHT:
                    (r,c,entry) = go_left(r,c,entry)

    visited_no_direction = set()
    for (r,c,_) in visited:
        visited_no_direction.add((r,c))

    print(f'part 1: {len(visited_no_direction)}')

'''
# Part 2

Now we want to try every possible entry to the grid, and find the one that will
light up the most squares. 

## Approach
So I built all this stuff thinking that this was going to need to be optimized, 
and int the process I finally learned a lot about how recursion (doesn't) work 
in Python, and then eventually I just ran the code on the test input without
any of the optimization, and it ended in a very reasonable time. 
So my approach ended up being to apply the code from part 1 to each option and take
the one with the longest path. But there's a bunch of extra code here that could 
be optimization someday.
'''
class MapTraversal:
    map = list[str]
    lights_from_here: dict

    def __init__(self, map):
        # this doesn't do anything but in theory it could be a lookup
        # table of {(r,c,entrypoint): number of tiles that light up from that combo} 
        self.lights_from_here = {}
        self.map = map

    #returns the numer of tiles that will light up starting from this point. 
    def traverse(self,r,c,entry):
        if (r,c,entry) not in self.lights_from_here:
            self.lights_from_here[(r,c,entry)] = self.really_traverse(r,c,entry)
        return self.lights_from_here[(r,c,entry)]

    def really_traverse(self,r,c,entry):
            # format will be (r,c,entry)
            visited = set()

            # store branches to come back to later
            queue = []

            #follow the path
            while (r,c,entry) not in visited or len(queue) > 0:
                if (r,c,entry) in visited:
                    (r,c,entry) = queue.pop()
                    if (r,c,entry) in visited:
                        continue

                visited.add((r,c,entry))

                match input[r][c]:
                    case '|':
                        if entry == LEFT or RIGHT:
                            previous=(r,c,entry)
                            (r,c,entry) = go_up(r,c,entry)
                            queue.append(go_down(*previous))
                        elif entry == BOTTOM:
                            (r,c,entry) = go_up(r,c,entry)
                        elif entry == TOP:
                            (r,c,entry) = go_down(r,c,entry)
                    case '-':
                        if entry == TOP or BOTTOM:
                            previous=(r,c,entry)
                            (r,c,entry) = go_left(r,c,entry)
                            queue.append(go_right(*previous))
                        elif entry == LEFT:
                            (r,c,entry) = go_right(r,c,entry)
                        elif entry == RIGHT:
                            (r,c,entry) = go_left(r,c,entry)
                    case '\\':
                        if entry == LEFT:
                            (r,c,entry) = go_down(r,c,entry)
                        elif entry == BOTTOM:
                            (r,c,entry) = go_left(r,c,entry)
                        elif entry == TOP:
                            (r,c,entry) = go_right(r,c,entry)
                        elif entry == RIGHT:
                            (r,c,entry) = go_up(r,c,entry)
                    case '/':
                        if entry == LEFT:
                            (r,c,entry) = go_up(r,c,entry)
                        elif entry == BOTTOM:
                            (r,c,entry) = go_right(r,c,entry)
                        elif entry == TOP:
                            (r,c,entry) = go_left(r,c,entry)
                        elif entry == RIGHT:
                            (r,c,entry) = go_down(r,c,entry)
                    case '.':
                        if entry == LEFT:
                            (r,c,entry) = go_right(r,c,entry)
                        elif entry == BOTTOM:
                            (r,c,entry) = go_up(r,c,entry)
                        elif entry == TOP:
                            (r,c,entry) = go_down(r,c,entry)
                        elif entry == RIGHT:
                            (r,c,entry) = go_left(r,c,entry)

            visited_no_direction = set()
            for (r,c,_) in visited:
                visited_no_direction.add((r,c))

            # print(visited)
            return len(visited_no_direction)        
        
def part2():

    map = MapTraversal(input)

    top = [map.traverse(0,n,TOP) for n in range(len(input[0]))]
    bottom = [map.traverse(len(input)-1,n,BOTTOM) for n in range(len(input[0]))]
    left = [map.traverse(n,0,LEFT) for n in range(len(input))]
    right = [map.traverse(n,len(input[0])-1,RIGHT) for n in range(len(input))]

    print(f'part 2: {max([*top, *bottom, *left, *right])}')

part1()
part2()