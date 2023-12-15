

with open('D15.txt', 'r') as file:
    input = file.read().split(',')

"""
# Part 1

## input
a line if codes seperated by commas:
    rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7

## Objective
for each code, we want to subject it to the following hash 
algorithm Starting with a current value of zero, for each
character in the code:
    - add the ascii value of the character to the current value
    - multiply the entire current value by 17
    - take the remainder of dividing the current value by 256
    as the new current value

the puzzle solution is the sum of hashing all the codes in the input

## Approach
we can just follow the steps as written to get the answer in a timely 
enough manner
    
"""
def part1():
    def hash(code):
        current = 0
        for char in code:
            current+=ord(char)
            current=current*17 % 256
        return current

    print(f'part1: {sum([hash(code) for code in input])}')

part1()