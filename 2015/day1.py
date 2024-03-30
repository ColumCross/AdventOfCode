#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_file = "input.txt"

with open(input_file, "r") as f:
    input_values = [n for n in f.read()]

# ------------------ #

floor = 0
position = 1

for instruction in input_values:
    if instruction == "(":
        floor += 1
    else:
        floor -= 1
    
    if floor == -1:
        print("First got to the basement at position " + str(position) + ".")

    position += 1

print("Santa is on floor " + str(floor) + ".")
