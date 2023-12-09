'''
# PART 1

## Input
Each line is an increasing list of numbers. For example:
    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45

## Objective
For each list, we want to find the next value in the sequence. We can extrapolate 
that by finding the differences between the values in the sequence, and the 
differences between the differences. and adding the next value to each of those
lists of differences, for example the first row of the above example looks like
this:
0   3   6   9  12  15  18
  3   3   3   3   3   3
    0   0   0   0   0

The third row is more complicated and you have to caluculate more differences, 
like this:

10  13  16  21  30  45  68
   3   3   5   9  15  23
     0   2   4   6   8
       2   2   2   2
         0   0   0

Our solution is the sum of the next number in each sequence in our input

'''

with open('D09.txt', 'r') as file:
    input = [[int(num) for num in line.split()] for line in file.read().splitlines()]

def part1():
    def next(seq):
        lines = []
        new_line = seq
        # find all the lists of differences, until we hit a flat line
        while sum([0 if num == 0 else 1 for num in new_line]) != 0:
            lines.append(new_line[:])
            new_line = [new_line[n] - new_line[n-1] for n in range(1, len(new_line))]
            print(new_line)
        # the next number in the initial list is the sum of the last number
        # in all the lists of differences that we found.
        return sum([line[-1] for line in lines])

    print(f'part 1: {sum([next(seq) for seq in input])}')

'''
# PART 2

Let's also subtract the initial differences from the first elements to get 
a previous element.

'''
def part2():
    def previous(seq):
        lines = [seq]
        new_line = seq
        # find all the lists of differences, until we hit a flat line
        while sum([0 if num == 0 else 1 for num in new_line]) != 0:
            new_line = [new_line[n] - new_line[n-1] for n in range(1, len(new_line))]
            lines.append(new_line[:])
            print(new_line)
        # subtract each starting difference from the first element in the previous list
        accumulator = 0
        for n in range(len(lines)-1, 0, -1):
            accumulator = lines[n-1][0] - accumulator
        return accumulator

    print(f'part 2: {sum([previous(seq) for seq in input])}')

part1()
part2()