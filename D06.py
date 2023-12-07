import re
import math

'''
# PART ONE 

## input 
Input represents a list of records that have been set by 
competitors in toy boat races. The time is in the first row,
with the record-setting distance for each time directly below.

For example
    Time:      7  15   30
    Distance:  9  40  200

## Puzzle description 
In these races, time is the constant and the distance traveled 
in that time is what we want to maxize. The speed of the toy
boat increases by 1 mm/milisecond for every second that you hold
down the button before you let the boat loose. 

Secifically, our boat will go 1 mm/milisecond faster for each second
that the button is held down before it starts moving. 

Our goal is to find how many different ways we could beat the 
record-holding distance for each race, and multiply them all 
together to solve the puzzle.

##Approach
the maximium possible distance for any time is going to be when 
you hold the button for 1/2 of the total possible time, and all possible
combinations can be represented by the quadratic function 
    distance = -(button_time^2 - TOTAL_TIME(button_time))

our task is to find how many integers fall in the range between the two button 
times that would produce the record distance

we can use the quadratic formula to find those two button times, and calculate the 
difference between them.
'''
def part1():
    with open('D06.txt', 'r') as file:
        [times_str, dist_str] = [line.split(":")[1].strip() for line in file.read().split(('\n'))]
        times = re.split(" +", times_str)
        dists = re.split(" +", dist_str)
        data=[(int(times[n]), int(dists[n])) for n in range(len(times))]
    print(data)

    results = []

    for(total_time, dist) in data:
        upper_bound = math.ceil(-(-total_time - math.sqrt((total_time * total_time) - (4*dist)))/2)
        lower_bound = math.floor(-(-total_time + math.sqrt((total_time * total_time) - 4*dist))/2)
        results.append(upper_bound - lower_bound - 1)

    print(math.prod(results))


'''
# PART 2
 
 just kidding, that sample input is all one race, with time = 71530 and distance = 940200

 ## Approach
 The approach I used in part 1 should still work.

'''
def part2():
    with open('D06.txt', 'r') as file:
        [times_str, dist_str] = [line.split(":")[1].strip() for line in file.read().split(('\n'))]
        times = re.split(" +", times_str)
        dists = re.split(" +", dist_str)
        total_time = int(''.join(times))
        dist = int(''.join(dists))

        upper_bound = math.ceil(-(-total_time - math.sqrt((total_time * total_time) - (4*dist)))/2)
        lower_bound = math.floor(-(-total_time + math.sqrt((total_time * total_time) - 4*dist))/2)
        print(upper_bound - lower_bound - 1)

part2()