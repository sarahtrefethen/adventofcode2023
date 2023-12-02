
from math import prod

'''
PART ONE
Each line of input represents a game involving a bag with an unknown 
number of red, blue, and green cubes. The elf shows you a few handfulls
of cubes from the bag, returning the cubes to the bag after you have 
seen them. We are looking for games where we never see more than
12 red cubes, 13 green cubes, or 14 blue cubes. Return value is the sum
of the IDs of each game that meets that criteria.

Approach: iterate over each line and check for handfulls of cubes that contain
more than the allowed number of cubes of any one color.
'''
def part1():
    MAXES = {'red': 12, 'green': 13, 'blue': 14}

    def return_id_if_possible(game):
        handfuls = game.split(': ')[1].split('; ')
        for handful in handfuls:
            for c in handful.split(", "):
                [num, color] = c.split(" ")
                if int(num) > MAXES[color]: 
                    return 0
        # the id is in the origional string in the form 'Game {id}: ...'
        return int(game.split(': ')[0].split(' ')[1])


    with open("D02input.txt", 'r') as file:
        input = file.read()
        print('part 1: ' + sum([return_id_if_possible(game) for game in input.split('\n')]))

'''
PART TWO
Now we want to find the minimum number of cubes of each color that could
have been in the bag for each game. This is equal to the maximum number 
of cubes of each color produced from the bag in any one handful over the 
course of the game. The power of a set of cubes is equal to the minimum numbers 
of red, green, and blue cubes multiplied together. We want to return the sum
of the powers of each game listed in the input. 

Approach: iterate over each game, find the max number of cubes of each
color produced in each game, and do all the arithmetic. 
'''
def part2():

    def return_power(game):
        handfuls = game.split(': ')[1].split('; ')
        maxes = {'red': 0, 'green': 0, 'blue': 0}    
        for handful in handfuls:
            for c in handful.split(", "):
                [num, color] = c.split(" ")
                if int(num) > maxes[color]: 
                    maxes[color] = int(num)
        return prod(maxes.values())


    with open("D02input.txt", 'r') as file:
        input = file.read()
        ret = sum([return_power(game) for game in input.split('\n')])
        print(f'part 2: {ret}')       


part1()
part2()
