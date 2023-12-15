from collections import defaultdict

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
def hash(code):
    current = 0
    for char in code:
        current+=ord(char)
        current=current*17 % 256
    return current


def part1():
    print(f'part1: {sum([hash(code) for code in input])}')

'''
# PART 2

Turns out the last part of the codes (either a '-', or a '=' followed by a number)
are instructions to either removed a labelled lens from an array of boxes in a 
or to add a lens with that label and focal length the the box. The little story
in the problem statement on the Advent of Code website is particularly cute today.

## Approach
As is strongly hinted in the story, this is a pretty straightforward hashmap 
implementation. We have to make sure to keep the entries in the map in order, because
their position is used to add everthing up for the puzzle answer. 
'''

class Hashmap:
    boxes: defaultdict

    def __init__(self):
        self.boxes=defaultdict(list)

    def add(self, box, label, lens):
        for idx in range(len(self.boxes[box])):
            if self.boxes[box][idx]['label'] == label:
                self.boxes[box][idx] = {'label': label, 'lens': int(lens)}
                break
        else:
            self.boxes[box].append({'label': label, 'lens': int(lens)})



    def remove(self, box, label):
        for idx in range(len(self.boxes[box])):
            if self.boxes[box][idx]['label'] == label:
                self.boxes[box].pop(idx)
                break

    def print(self):
        for key, value in self.boxes.items():
            print(f'box {key}: {value}')

    def add_up(self):
        total = 0
        for key, value in self.boxes.items():
            total += sum([(n+1)*(key+1)*value[n]['lens'] for n in range(len(value))])
        return total

def part2():

    map = Hashmap()
    for code in input:
        if "=" in code:
            [label, lens] = code.split('=')
            box = hash(label)
            map.add(box, label, lens)
        elif '-' in code:
            label = code.rstrip('-')
            box = hash(label)
            map.remove(box, label)

    print(f'part2: {map.add_up()}')

part1()
part2()