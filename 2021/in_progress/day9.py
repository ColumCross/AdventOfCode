#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_file = "day9_"
# input_file += "test.txt"
input_file += "input.txt"

with open(input_file, "r") as f:
    input_values = [n for n in f.read().splitlines()]

cave_map = [[int(c) for c in r] for r in input_values]

low_points = []


def partOne():
    risk_levels = []
    
    y = 0
    while y < len(cave_map):

        x = 0
        while x < len(cave_map[y]):
            above = checkAbove(x, y)
            below = checkBelow(x, y)
            left = checkLeft(x, y)
            right = checkRight(x, y)
            
            # # try:
            # above = checkAbove(x, y)
            # # except:
            # #     above = True

            # try:
            #     below = checkBelow(x, y)
            # except:
            #     below = True

            # try:
            #     left = checkLeft(x, y)
            # except:
            #     left = True

            # try:
            #     right = checkRight(x, y)
            # except:
            #     right = True

            if above and below and left and right:
                risk_levels.append(cave_map[y][x] + 1)
                low_points.append([x,y])
                # total_risk_level += risk_level

            x += 1

        y += 1

    # print(str(risk_levels))
    total_risk_level = sum(risk_levels)


    # print(cave_map)
    return total_risk_level
       
def checkAbove(x, y):
    if y == 0:
        return True
    else:
        check = cave_map[y][x]
        against = cave_map[y-1][x]
        return check < against

def checkBelow(x, y):
    try:
        check = cave_map[y][x]
        against = cave_map[y+1][x]
        return check < against
    except IndexError:
        return True

def checkLeft(x, y):
    if x == 0:
        return True
    else:
        check = cave_map[y][x]
        against = cave_map[y][x-1]
        return check < against

def checkRight(x, y):
    try:
        check = cave_map[y][x]
        against = cave_map[y][x+1]
        return check < against
    except IndexError:
        return True

def partTwo():
    basin_sizes = []
    print(str(low_points))

    for lowpoint in low_points:
        x = lowpoint[0]
        y = lowpoint[1]

        basin_size = 0
        # basin_size += countAbove(x, y-1)
        # basin_size += countBelow(x, y+1)
        # basin_size += countLeft(x-1, y)
        # basin_size += countRight(x+1, y)

        basin_size += count(x, y)

        basin_sizes.append(basin_size)

    print(str(basin_sizes))
    basin_sizes.sort(reverse = True)
    answer = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    print("The answer to part 2 is: " + str(answer))

def countAbove(x, y):
    if y < 0:
        return 0
    else:
        check = cave_map[y][x]
        if check == 9:
            return 0
        else:
            return 1 + countAbove(x, y-1)

def countBelow(x, y):
    try:
        check = cave_map[y][x]
        newy = y+1
        if check == 9:
            return 0
        else:
            return 1 + countBelow(x, newy)
    except IndexError:
        return 0

def countLeft(x, y):
    if x < 0:
        return 0
    else:
        check = cave_map[y][x]
        newx = x-1
        if check == 9:
            return 0
        else:
            return 1 + countLeft(newx, y)

def countRight(x, y):
    try:
        check = cave_map[y][x]
        if check == 9:
            return 0
        else:
            return 1 + countRight(x+1, y)
    except IndexError:
        return 0

def count(x, y):
    if x < 0 or y < 0:
        return 0

    try:
        check = cave_map[y][x]
        if check < 9:
            cave_map[y][x] = 10
            return 1 + count(x, y-1) + count(x, y+1) + count(x-1, y) + count(x+1, y)
        else:
            return 0
    except IndexError:
        return 0
    

message = "The answer to part one is: "
message += str(partOne())
print(message)

partTwo()