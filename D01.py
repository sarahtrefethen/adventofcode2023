


################## PART 1 #############################
'''
Input is a list of strings, each string on a new line in the input file. 
We need to find the calibration value for each line, defined as the 
two-digit number represented by the first and last numerical digit in 
each string, and then sum together all the calibration values in the file.
'''
def first_and_last_digit(line: str):
    digits = [char for char in line if char.isdigit()]
    return digits[0] + digits[len(digits) - 1]

def part_one():
    with open("D01input.txt", 'r') as input:
        text = input.read()
        calibration_values = [int(first_and_last_digit(l)) for l in text.split('\n')]
        print(f'part 1: {sum(calibration_values)}')

################## PART 2 #############################
'''
Input is a list of strings, each string on a new line in the input file. 
We need to find the calibration value for each line, defined as the 
two-digit number represented by the first and last numerical digit 
OR number written out in english (ie, "one", "two", ect) in 
each string, and then sum together all the calibration values in the file.
'''
    
word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def first_number(line):
    for idx in range(len(line)):
        if line[idx].isdigit():
            return line[idx]
        for word in list(word_to_digit):
            if line[idx:].startswith(word):
                return word_to_digit[word]
    print(f'did not find a first in {line}')
        
def last_number(line):
    for idx in range(len(line), 0, -1):
        if line[idx-1].isdigit():
            return line[idx-1]
        for word in list(word_to_digit):
            if line[:idx].endswith(word):
                return word_to_digit[word]
    print(f'did not find a last in {line}')
    

def part_two():
    with open("D01input.txt", 'r') as input:
        text = input.read()
        calibration_values = [int(first_number(l) + last_number(l)) for l in text.split('\n')]
        print(f'part 2: {sum(calibration_values)}')

part_one()
part_two()