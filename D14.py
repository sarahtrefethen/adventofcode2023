'''
# PART 1

## Input
We are provided with a grid of rocks and open space:
    O....#....
    O.OO#....#
    .....##...
    OO.#O....O
    .O.....O#.
    O.#..O.#.#
    ..O..#O..O
    .......O..
    #....###..
    #OO..#....
The '0's are rocks that will roll and the '#'s are rocks that
are fixed in place. When we tip the platform represented by this
grid upwards, towards the north, the rocks rearrange to look like 
this: 
    OOOO.#.O..
    OO..#....#
    OO..O##..O
    O..#.OO...
    ........#.
    ..#....#.#
    ..O..#.O.O
    ..O.......
    #....###..
    #....#....

## Objective
We want to add up 'weights' of each round stone, starting with a weight
equal to the number of rows (10 in the example) for each stone in the top row
and one less for each stone in each subsequent row.

## Approach
This is easier to thing about if we rotate the grid so that each column 
is a list that we can parse. Then it is simply a matter of counting how many 
round stones lie between the static stones and the edges of the grid, and 
then calulating their weights based on where they would land.
'''



with open('D14.txt', 'r') as file:
    grid = file.read().splitlines()

cols = [[grid[x][y] for x in range(len(grid))] for y in range(len(grid[0]))]

def weigh_slided_rocks(col):
    ret = 0
    previous_block = -1
    block_index = col.index("#") if "#" in col else len(col)
    while True:
        if block_index == previous_block:
            return ret
        count = col[previous_block+1 :  block_index].count('O')
        # print(f'found {count} rocks in this section')
        add = sum(range(len(col) - previous_block -count, len(col) - previous_block))
        # print(f'adding {add}')
        ret += add
        previous_block = block_index
        try:
            block_index = col.index('#', previous_block+1)
        except:
            block_index = len(col)
        
print(f'part 1: {sum([weigh_slided_rocks(col) for col in cols])}')