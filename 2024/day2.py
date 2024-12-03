#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input_file = "test.txt" if sys.argv[1] == "t" else "input.txt"

with open(input_file, "r") as f:
    input_values = [n.split(" ") for n in f.read().splitlines()]

# ------------------ #

def checkLevels(level):
    # Check if the level is sorted in either direction
    if(all(int(level[i]) <= int(level[i + 1]) for i in range(len(level) - 1)) or all(int(level[i]) >= int(level[i + 1]) for i in range(len(level) - 1))):
        
        # Check if the levels change is gradual
        if(all(0 < abs(int(level[i+1]) - int(level[i])) <= 3 for i in range(len(level) - 1))):
            return True
        else:
              return False
        
    else:
        return False

p1ans = 0
p2ans = 0

for level in input_values:
    if(checkLevels(level)):
        p1ans += 1
        p2ans += 1

    # For part 2
    # Check each failed iteration by removing one element
    else:
        i = 0
        while i < len(level):
            newLevel = level.copy()
            del newLevel[i]
            if(checkLevels(newLevel)):
                p2ans += 1
                break
            else:
                i += 1
            
print("Part One Answer:")
print(p1ans)
print("-----")
print("Part Two Answer:")
print(p2ans)
print("-----")