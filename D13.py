'''
# Part 1

## input
for example: 
    #.##..##.
    ..#.##.#.
    ##......#
    ##......#
    ..#.##.#.
    ..##..##.
    #.#.##.#.

    #...##..#
    #....#..#
    ..##..###
    #####.##.
    #####.##.
    ..##..###
    #....#..#

we want to find a single line of either verticle or horizontal symetry in 
each grid in the input. Depending on how far from the edge the line is, 
some rows or columns will not be included. For example, if the line of symetry
were between the first and second columns, only those two columns would be included.

## Approach
Because there is only one result for each input, we can just iterate through the grid
until we find a row or column that meets the criteria. 
'''

with open('D13.txt', 'r') as file:
    input = [block.splitlines() for block in file.read().split('\n\n')]

def part1():
    def score(grid):

        #check for horizontal reflection
        for c in range(1, len(grid[0])):
            # print(f'*****checking col {c} for a pivot***')
            for r in range(0, len(grid)):
                start = 2*c-len(grid[0]) if 2*c-len(grid[0]) > 0 else 0
                if grid[r][start:c] != grid[r][(2*c)-1:c-1:-1]:
                    # we found an asymetry, this isn't the column
                    break
            else:
                # print(f'found mirrir at col {c}')
                return c

        #check for vertical reflection
        for r in range(1, len(grid)):
            # print(f'*****checking row {r} for a pivot***')
            for c in range(0, len(grid[r])):
                col = [grid[n][c] for n in range(len(grid))]
                start = 2*r-len(grid) if 2*r-len(grid) > 0 else 0
                if col[start:r] != col[(2*r)-1:r-1:-1]:
                    # we found an asymetry, this isn't the row
                    break
            else:
                # print(f'found mirrir at row {r}')
                return r*100
    print(f'part 1: {sum([score(grid) for grid in input])}')

part1()