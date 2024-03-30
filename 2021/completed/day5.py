#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


#input_file = "test.txt" # if sys.argv[1] == 1 else "input.txt"
input_file = "day5_input.txt"

with open(input_file, "r") as f:
    input_values = [n for n in f.read().splitlines()]

# ------------------ #

def partTwo():
    
    functions = buildList()
    grid = [[0 for c in range(1000)] for r in range(1000)]
    answer = 0

    #print(functions)

    x = 0
    while x < 1000:
        y = 0
        while y < 1000:
            for f in functions:
                
                if f["slope"] == "X":
                    if x != f["x1"]:
                        continue

                    if y in range(f["y1"], f["y2"]+1) or y in range(f["y2"], f["y1"]+1):
                        grid[x][y] += 1
                        if grid[x][y] == 2:
                            answer += 1
                else:
                    xs = [f["x1"], f["x2"]]
                    ys = [f["y1"], f["y2"]]
                    xs.sort()
                    ys.sort()

                    if x not in range(xs[0], xs[1]+1) or y not in range(ys[0], ys[1]+1):
                        continue

                    m = f["slope"]
                    b = f["b"]
                    if y == m * x + b:
                        grid[x][y] += 1
                        if grid[x][y] == 2:
                            answer += 1


            y += 1

        print("After x coord " + str(x) + ", the number of intersects is " + str(answer))
        x += 1

    return answer

def buildList():
    
    functions = []

    for line in input_values:
        breakapart = line.split(" -> ")

        x1 = int(breakapart[0].split(",")[0])
        x2 = int(breakapart[1].split(",")[0])

        y1 = int(breakapart[0].split(",")[1])
        y2 = int(breakapart[1].split(",")[1])

        vent = {
            "x1": x1,
            "x2": x2,
            "y1": y1,
            "y2": y2,
        }

        try:
            slope = (y2 - y1) / (x2 - x1)
            b = y1 - (slope * x1)

            vent["slope"] = int(slope)
            vent["b"] = int(b)
        except ZeroDivisionError:
            vent["slope"] = "X"
        

        functions.append(vent)

    return functions

def partOne():

    functions = buildList()
    grid = [[0 for c in range(1000)] for r in range(1000)]
    answer = 0

    x = 0
    while x < 1000:
        y = 0
        while y < 1000:
            for f in functions:
                if f["slope"] == 0:
                    if y != f["y1"]:
                        continue

                    if x in range(f["x1"], f["x2"]+1) or x in range(f["x2"], f["x1"]+1):
                        grid[x][y] += 1
                        if grid[x][y] == 2:
                            answer += 1
                    # else:
                        # print("Not in range: " + str(x) + ", " + str(y))
                        # print(f)

                else:
                    if x != f["x1"]:
                        continue

                    if y in range(f["y1"], f["y2"]+1) or y in range(f["y2"], f["y1"]+1):
                        grid[x][y] += 1
                        if grid[x][y] == 2:
                            answer += 1
                    # else:
                        # print("Not in range: " + str(x) + ", " + str(y))
                        # print(f)


            y += 1
        x += 1

    return answer

print(partTwo())
