#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input_file = "test.txt"
input_file = "input.txt"

with open(input_file, "r") as f:
    input_values = [list(n) for n in f.read().splitlines()]

# ------------------ #

#print(input_values)

p1ans = 0
p2ans = 0

# Function that check if XMAS is there
def check(x, y, letter, xMod, yMod):
    levels = ["S", "A", "M", "X"]

    # Got out of bounds somehow
    if(x<0 or y<0): return False

    # Was trying to do it without relying on error handling, but that just was too much work.
    # Check if I hit a wall. If I did, it fails.
    try:
        val = input_values[y][x]
    except:
        return False

    if(val == levels[letter]):
        if(letter == 0):
            #print(x, y)
            #print(input_values[y][x] + input_values[y-yMod][x-xMod] + input_values[y-yMod-yMod][x-xMod-xMod] + input_values[y-yMod-yMod-yMod][x-xMod-xMod-xMod])
            return True
        else:
            return check(x+xMod, y+yMod, letter-1, xMod, yMod)
    else:
        return False
    

# Part 2
def checkX(x, y, sizeY, sizeX):

    # Needs to be in bounds
    if x < 1: return False
    if y < 1: return False
    if y > sizeY-2: return False
    if x > sizeX-2: return False

    corners = input_values[y-1][x-1] + input_values[y-1][x+1] + input_values[y+1][x-1] + input_values[y+1][x+1]
    possibilities = ["MSMS", "MMSS", "SSMM", "SMSM"]
    if corners in possibilities:
        return True
    else:
        return False

    
for y in range(0, len(input_values)):
    for x in range(0, len(input_values[y])):
        # Check up
        # Check down
        # Check left
        # Check right

        # Check diags

        if check(x, y, 3, 0, -1): p1ans += 1
        if check(x, y, 3, 0, 1): p1ans += 1
        if check(x, y, 3, -1, 0): p1ans += 1
        if check(x, y, 3, 1, 0): p1ans += 1

        if check(x, y, 3, 1, 1): p1ans += 1
        if check(x, y, 3, -1, 1): p1ans += 1
        if check(x, y, 3, 1, -1): p1ans += 1
        if check(x, y, 3, -1, -1): p1ans += 1

        if input_values[y][x] == "A":
            if checkX(x, y, len(input_values), len(input_values[y])): p2ans += 1


print("Part One Answer:")
print(p1ans)
print("-----")
print("Part Two Answer:")
print(p2ans)
print("-----")
        
      
        
            
        