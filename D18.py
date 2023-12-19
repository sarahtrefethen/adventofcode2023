'''
# PART 1

## Input
    R 6 (#70c710)
    D 5 (#0dc571)
    L 2 (#5713f0)
    D 2 (#d2c081)
    R 2 (#59c680)
    D 2 (#411b91)
    L 5 (#8ceee2)
    U 2 (#caa173)
    L 1 (#1b58a2)
    U 2 (#caa171)
    R 2 (#7807d2)
    U 3 (#a77fa3)
    L 2 (#015232)
    U 2 (#7a21e3)

## Objective 
the first two entries on each line in the input correspond to 
a direction and a distance. The elves have a digger that will 
remove 1 cubic unit of earth per step, and they plan to dig a ditch
following this pattern. Then, they will also excavate the earth
in the area surrounded by the ditch to a depth of 1 meter. What
is the total area of the pool they will create?

## Approach
I found an algorithm (shoestring algorithm) for finding the area
of a polygon from an ordered list of the points of its verteces, 
which is easily extrapolated from the data. After that, we just 
have to account for the area of the ditch, only slightly less than
half of which is contained in the results of the shoestring algorithm.
The volume of the ditch outside the shoestring result is half of 
the ditch volume plus two. to account for the four outer corners 
of the polygon.  (all the other corners cancel each other out)
'''

def lets_dig(part):

    with open('D18.txt', 'r') as file:
        if part == 1:
            input = [(l.split(" ")[0], int(l.split(" ")[1])) for l in file.read().splitlines()]
        else:
            hexcodes = [l.split(" ")[2].strip('(').strip(')') for l in file.read().splitlines()]
            input = [('RDLU'[int(code[-1])],int(code[1:6], 16)) for code in hexcodes]
    

    U = "U"
    D = "D"
    L = "L"
    R = "R"

    corners = []
    cur_r = 0
    cur_c = 0
    max_r = 0
    max_c = 0
    min_r = 0
    min_c= 0

    for i in range(len(input)):
        [dir, count] = input[i]
        if dir == U:
            cur_r -= count
            if cur_r < min_r:
                min_r = cur_r
        elif dir == D:
            cur_r += count
            if cur_r > max_r:
                max_r = cur_r
        elif dir == L:
            cur_c -= count
            if cur_c > min_c:
                max_c = max_c
        elif dir == R:
            cur_c += count
            if cur_c < min_c:
                min_c = cur_c
        corners.append((cur_r, cur_c))

    ditch = sum([dist for (dir, dist) in input])

    shoestring = 0
    for i in range(len(corners)):
        (pre_x,pre_y) = corners[i-1]
        (x,y) = corners[i]
        shoestring += ((pre_y*x) - (pre_x*y))/2 
    
    print(f'part {part}: {shoestring + (ditch / 2)+1}')

lets_dig(2)
    