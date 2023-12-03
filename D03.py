from collections import defaultdict
from math import prod

'''
# PART ONE

The elves need help with a broken gondola. 

## Input
> The engine schematic (your puzzle input) consists of a
> visual representation of the engine. There are lots of
> numbers and symbols you don't really understand, but
> apparently any number adjacent to a symbol, even diagonally,
> is a "part number" and should be included in your sum. 

for example: 
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

Here, only 114 and 58 are not part numbers. Some symbols are 
adjacent to more than one number. 

## Objective

Add up all the part numbers

## Approach

Read through the input in a single pass, keeping track of each
string of numbers and checking for an adjacent symbol. 
'''
def part1():

    with open("D03input.txt", "r") as file:
        schematic = file.read().split('\n')

    row_count = len(schematic)
    col_count = len(schematic[0])

    # helper function to search around a cell
    def has_adjacent_symbol(row, col):
        top_row = row - 1 if row > 0 else row
        left_col = col - 1 if col > 0 else col
        bottom_row = row + 1 if row < row_count - 1  else row
        right_col = col + 1 if col < col_count - 1 else col
        for r in range(top_row, bottom_row + 1):
            for c in range(left_col, right_col + 1):
                if not schematic[r][c].isalnum() and schematic[r][c] != '.':
                    return True
        return False

    # keep track of all the part numbers we find
    part_numbers = []

    # keep track of what is happening from one cell to the next
    current_num = ''
    current_num_is_part_number = False
    
    for row_index in range(row_count):
        row = schematic[row_index]
        for col_index in range(col_count):
            if row[col_index].isdigit():
                current_num = current_num + row[col_index]
                if not current_num_is_part_number:
                    current_num_is_part_number = has_adjacent_symbol(row_index, col_index)
            elif current_num != '':
                if current_num_is_part_number:
                    part_numbers.append(int(current_num))
                current_num = ''
                current_num_is_part_number = False

    print(f'part 1: {sum(part_numbers)}')

'''
# PART TWO
 
 This time, we are searching the gondola parts looking for gears only.
 Gears are marked with an * and have more than one adjacent number. We 
 want to find the product of all the numbers adjacent to each gear 
 (the gear ratio) and add them together.

 ## Approach
 Modify previous code to only care about *, and organize the numbers
 by the id of their adjacent *. We will define a gear's id as <row>.<col>.

'''

def part2():

    with open("D03input.txt", "r") as file:
        schematic = file.read().split('\n')

    row_count = len(schematic)
    col_count = len(schematic[0])

    # helper function to search around a cell
    def find_adjacent_gear(row, col):
        top_row = row - 1 if row > 0 else row
        left_col = col - 1 if col > 0 else col
        bottom_row = row + 1 if row < row_count - 1  else row
        right_col = col + 1 if col < col_count - 1 else col
        for r in range(top_row, bottom_row + 1):
            for c in range(left_col, right_col + 1):
                if schematic[r][c] == '*':
                    return (f'{r}.{c}')
        return False

    # keep track of all potential gear ids and their numbers
    gears = defaultdict(list)

    # keep track of what is happening from one cell to the next
    current_num = ''
    current_gear_id = False
    
    # read through the input one cell at a time and record all 
    # the numbers adjacent to * characters.
    for row_index in range(row_count):
        row = schematic[row_index]
        for col_index in range(col_count):
            if row[col_index].isdigit():
                current_num = current_num + row[col_index]
                if not current_gear_id:
                    current_gear_id = find_adjacent_gear(row_index, col_index)
            elif current_num != '':
                if current_gear_id:
                    gears[current_gear_id].append(int(current_num))
                current_num = ''
                current_gear_id = False

    gear_ratios = [prod(nums) for nums in gears.values() if len(nums) > 1]
    print(f'part 2: {sum(gear_ratios)}')

part1()
part2()