'''
#Part 1

## input
the # in this grid represent stars in a galaxy
    ...#......
    .......#..
    #.........
    ..........
    ......#...
    .#........
    .........#
    ..........
    .......#..
    #...#.....

## Objective
we want to find the sum of the shortest paths between each 
of the stars, but the catch is that the stars are moving apart.
For each row or column that has no stars, we should double that 
row or column.

## Approach
First we find the empty rows and columns.
Then we find the coordinates of each star in the origional map.
Then we increment the coordinates based on the expanded rows 
and columns.
'''

with open('D11.txt', 'r') as file:
    input = [[char for char in line] for line in file.read().splitlines()]

double_rows = []
star_coordinates = []
for i in range(len(input)):
    if sum([0 if char == '.' else 1 for char in input[i]]) == 0:
        double_rows += [i]
    else:
        previous_idx = -1
        for n in range(input[i].count('#')):
            new_index = input[i].index('#', previous_idx+1, len(input[i]))
            star_coordinates += [[i, new_index]]
            previous_idx = new_index 
double_cols = []
for i in range(len(input[0])):
    if sum([0 if char == '.' else 1 for char in [input[n][i] for n in range(len(input))]]) == 0:
        double_cols += [i]

print(star_coordinates)

print(double_rows)
coord_pointer = 0
for idx in range(len(double_rows)):
    while star_coordinates[coord_pointer][0] < double_rows[idx]:
        star_coordinates[coord_pointer][0] += idx
        coord_pointer+=1
while coord_pointer < len(star_coordinates):
    star_coordinates[coord_pointer][0] += len(double_rows)
    coord_pointer+=1
print(star_coordinates)

star_coordinates.sort(key=lambda coord: coord[1])
print(double_cols)
coord_pointer = 0
for idx in range(len(double_cols)):
    while star_coordinates[coord_pointer][1] < double_cols[idx]:
        star_coordinates[coord_pointer][1] += idx
        coord_pointer+=1
while coord_pointer < len(star_coordinates):
    star_coordinates[coord_pointer][1] += len(double_cols)
    coord_pointer+=1

print(star_coordinates)

distances = []
for i in range(len(star_coordinates)):
    for j in range(i+1, len(star_coordinates)):
        a = star_coordinates[i]
        b = star_coordinates[j]
        distances.append(abs(a[0]-b[0])+ abs(a[1]-b[1]))

print(sum(distances))



# for line in input:
#     print(line)