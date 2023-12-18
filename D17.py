'''
# PART 1

## input 
    2413432311323
    3215453535623
    3255245654254
    3446585845452
    4546657867536
    1438598798454
    4457876987766
    3637877979653
    4654967986887
    4564679986453
    1224686865563
    2546548887735
    4322674655533

## objective 
minimized the total numbers traversed from the upper left to the lower
right corner. You can never go more than three spaces in a straight line
before turning 90 degrees.

## Approach
Dijkstra's Algorithm is the way to find a shortest path, but this stuff
about the turning distances is a complication. I am thinking of multiple 
"nodes" on the graph for each square on the grid, one for each possible way 
you can enter the node (distance and direction combined.)
Reading about the algorithim online, it seems you're supposed to be able to
only directly inspect each reachable node once, but I found that that didn't give 
me complete coverage. So there's a bug in here somewhere, but I was able 
to get the correct answer by reinspecting nodes.

# PART 2
same situation, but now the machine has to go at least 4 squares in one 
direction before it can turn (or stop at the end) and can go at most 
nine squares without turning.

## Approach
I was able to slightly modify my part 1 code to work for part 2.
'''

with open('D17.txt', 'r') as file:
    input = [[int(c) for c in line] for line in file.read().splitlines()]

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def neighbors(node):
    # returns the legal next steps for the current node
        [cur_r, cur_c, cur_entry, cur_s] = node
        if cur_entry == None:
            return [(cur_r+1, cur_c, UP,1), (cur_r, cur_c+1, LEFT,1)]
        else:
            # all avaliable next steps, not considering the three step rule
            possibles = []
            for dir in [UP,DOWN,LEFT,RIGHT]:
                if dir != cur_entry:
                    if dir == UP and cur_r != 0:
                        possibles.append((cur_r-1, cur_c, DOWN))
                    if dir == DOWN and cur_r != len(input)-1:
                        possibles.append((cur_r+1, cur_c, UP))
                    if dir == LEFT and cur_c != 0:
                        possibles.append((cur_r, cur_c-1, RIGHT))
                    if dir == RIGHT and cur_c != len(input[0])-1:
                        possibles.append((cur_r, cur_c+1, LEFT))
            # make sure we're not going more than three squares on one direction
            # and add on the distance parameter
            ret = []
            for node in possibles:
                if node[2] == cur_entry:
                    if cur_s != 2:
                        ret.append((*node, cur_s+1))
                else:
                    ret.append((*node, 0))
            return ret


def neighbors_part2(node):
    # returns the legal next steps for the current node
        [cur_r, cur_c, cur_entry, cur_s] = node
        if cur_entry == None:
            return [(cur_r+1, cur_c, UP,1), (cur_r, cur_c+1, LEFT,1)]
        else:
            # all avaliable next steps, not considering machine's limitations
            possibles = []
            for dir in [UP,DOWN,LEFT,RIGHT]:
                if dir != cur_entry:
                    if dir == UP and cur_r != 0:
                        possibles.append((cur_r-1, cur_c, DOWN))
                    if dir == DOWN and cur_r != len(input)-1:
                        possibles.append((cur_r+1, cur_c, UP))
                    if dir == LEFT and cur_c != 0:
                        possibles.append((cur_r, cur_c-1, RIGHT))
                    if dir == RIGHT and cur_c != len(input[0])-1:
                        possibles.append((cur_r, cur_c+1, LEFT))
            # filter out possibilities that don't adhear to machine limitations
            ret = []
            for node in possibles:
                if node[2] == cur_entry:
                    if cur_s != 9:
                        ret.append((*node, cur_s+1))
                elif cur_s > 2:
                    ret.append((*node, 0))
            return ret



def search(part):
    target_row = len(input) - 1
    target_col = len(input[0]) -1

    unvisited = set()
    for r in range(len(input)):
        for c in range(len(input[0])):
            for dir in [UP, DOWN, LEFT, RIGHT]:
                for steps in range(3):
                    unvisited.add((r,c,dir,steps))    

    start = (0,0,None,0)

    nodes = [start]
    unvisited.add(start)
    distances = {start: 0}
    previous = {start: None}

    paths_to_goal = []

    while len(nodes):
        node = nodes.pop(0)
        neighbs = neighbors(node) if part == 1 else neighbors_part2(node)
        for neighbor in neighbs:
            #distance to the neighbor through the current node
            new_distance = distances[node] + input[neighbor[0]][neighbor[1]]
            if neighbor not in distances:
                distances[neighbor] = new_distance
                previous[neighbor] = node
                nodes.append(neighbor)
            elif distances[neighbor] > new_distance:
                distances[neighbor] = new_distance
                previous[neighbor] = node
                nodes.append(neighbor)
            if neighbor[:2] == (target_row, target_col):
                if part == 1:
                    paths_to_goal.append(distances[neighbor])
                # extra condition for part 2
                elif neighbor[3] > 2:
                    paths_to_goal.append(distances[neighbor])
        
    print(f'part {part}: {min(paths_to_goal)}')

search(1)
search(2)