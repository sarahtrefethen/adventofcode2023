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

part1()