'''
# PART 1

## Input
for example:
    ...........
    .....###.#.
    .###.##..#.
    ..#.#...#..
    ....#.#....
    .##..S####.
    .##..#...#.
    .......##..
    .##.#.####.
    .##..##.##.
    ...........

## Objective
Caluculate how manys different dots are reachable in n steps from
S. you can only traverse dots, not hashes. Backtracking is allowed.

## Approach
for each path, we only need to keep track of the current location
at any given step. 
Paths that land on the same point at the same step can be treated
as identical. 
'''

with open("D21.txt", "r") as file:
    input = file.read().splitlines()

for r in range(len(input)):
    line = input[r] 
    if "S" in line:
        start = (r, line.index('S'))
    print(line)

print(f'starting at {start}')

def part1():
    current = [start]

    for step in range(64):
        new_locations = set()
        while(len(current)):
            (r,c) = current.pop()
            if r != 0 and (input[r-1][c] == '.' or input[r-1][c] == 'S'):
                new_locations.add((r-1, c))
            if r != len(input)-1 and (input[r+1][c] == '.' or input[r+1][c] == 'S'):
                new_locations.add((r+1, c))
            if c != 0 and (input[r][c-1] == '.' or input[r][c-1] == 'S'):
                new_locations.add((r, c-1))
            if c != len(input[0])-1 and (input[r][c+1] == '.' or input[r][c+1] == 'S'):
                new_locations.add((r, c+1))
        current = list(new_locations)

    print(f'part 1: {len(current)}')
        
    # for r in range(len(input)):
    #     line = ""
    #     for c in range(len(input[r])):
    #         if (r,c) in current:
    #             line += '0'
    #         else:
    #             line += input[r][c]
    #     print(line)

part1()