#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input = "0"

p1ans = 0
p2ans = 0

# ----------------- #

stones = input.split()

def transmute(stones):
    newStones = []
    for stone in stones:
        if(stone == "0"):
            newStones.append("1")
        elif(len(stone) % 2 == 0):
            # Get the portion of the stone (before or after) the mid point (half the length cast as an int),
            # then cast it as an int to remove leading 0s, then cast it back as a string,
            # then append that string to the new stones
            newStones.append(str(int(stone[:int(len(stone)/2)])))
            newStones.append(str(int(stone[int(len(stone)/2):])))
        else:
            newStone = int(stone) * 2024
            newStones.append(str(newStone))
    return newStones

for x in range(1, 76):
    stones = transmute(stones)
    print("After ",x," blinks:")
    print(len(stones))
