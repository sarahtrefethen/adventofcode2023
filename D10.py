'''
# PART 1

## Input
We are giving a grid of text representing a map of pipes, some 
of which connect together to form a loop. The look starts at 
the one 'S' in the grid and contains the following other symbols:
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.

sample input looks like this:
    7-F7-
    .FJ|7
    SJLL7
    |F--J
    LJ.LJ

Approach: Just follow the path from the start till we get back 
again and halve the distance. Would be faster to have two pointers
but too hard to code. 
'''

VERT = "|"
HORZ = "-"
DOWN_RIGHT = LEFT_UP = "L"
DOWN_LEFT = RIGHT_UP = "J"
UP_LEFT = RIGHT_DOWN = "7"
UP_RIGHT = LEFT_DOWN = 'F'

with open('D10.txt', 'r') as file:
    input = [[char for char in line] for line in file.read().splitlines()]

######### helper functions and constants #####

def find_start():
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == 'S':
                return (row, col)

def symbol_at(location):
    return (input[location[0]][location[1]])

# When I wrote these I thought i was going to use them 
# more than the once time evaluating the start point, 
# but they are still useful
def connects_above(row, col):
    return input[row][col] in [VERT, UP_RIGHT, UP_LEFT]
def connects_left(row, col):
    return input[row][col] in [HORZ, LEFT_DOWN, LEFT_UP]
def connects_below(row, col):
    return input[row][col] in [VERT, DOWN_LEFT, DOWN_RIGHT]
def connects_right(row, col):
    return input[row][col] in [HORZ, RIGHT_DOWN, RIGHT_UP]

TOP = 'top'
BOTTOM = 'bottom'
LEFT = 'left'
RIGHT = 'right'

def go_up(current):
    current = (current[0]-1, current[1])
    entry_point = BOTTOM
    return (current, entry_point)

def go_left(current):
    current = (current[0], current[1]-1)
    entry_point = RIGHT
    return (current, entry_point)

def go_right(current):
    current = (current[0], current[1]+1)
    entry_point = LEFT
    return (current, entry_point)

def go_down(current):
    current = (current[0]+1, current[1])
    entry_point = TOP
    return (current, entry_point)

############ find the starting point####
# the starting point is a special case because
# we don't know it's symbol, so we need to look
# at the neighboring squares to infer which way 
# we should go 
start = find_start()
(start_row, start_col) = start

if start_row != 0 and connects_above(start_row-1, start_col):
    current=(start_row-1, start_col)
    entry_point = BOTTOM
elif start_col != 0 and connects_left(start_row, start_col-1):
    current = (start_row, start_col-1)
    entry_point = RIGHT
elif start_row != len(input) - 1 and connects_below(start_row + 1, start_col):
    current = (start_row + 1, start_col)
    entry_point = TOP

######## follow to path until we are back at the start ##
previous = start
steps = 1

while (current != start or steps == 1):
    steps+=1
    symbol = symbol_at(current)
    print(symbol_at(current))
    print(current)
    print(entry_point)

    if entry_point == TOP:
        if symbol == DOWN_LEFT:
            (current, entry_point) = go_left(current)
        elif symbol == DOWN_RIGHT:
            (current, entry_point) = go_right(current)
        elif symbol == VERT:
            (current, entry_point) = go_down(current)
    elif entry_point == RIGHT:
        if symbol == LEFT_UP:
            (current, entry_point) = go_up(current)
        elif symbol == LEFT_DOWN:
            (current, entry_point) = go_down(current)
        elif symbol == HORZ:
            (current, entry_point) = go_left(current)
    elif entry_point == BOTTOM:
        if symbol == UP_LEFT:
            (current, entry_point) = go_left(current)
        elif symbol == UP_RIGHT:
            (current, entry_point) = go_right(current)
        elif symbol == VERT:
            (current, entry_point) = go_up(current)
    elif entry_point == LEFT:
        if symbol == RIGHT_UP:
            (current, entry_point) = go_up(current)
        elif symbol == RIGHT_DOWN:
            (current, entry_point) = go_down(current)
        elif symbol == HORZ:
            (current, entry_point) = go_right(current)

print(f'part1: {steps/2}')

