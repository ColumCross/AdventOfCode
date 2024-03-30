#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


# input_file = "test.txt" if sys.argv[0] == 1 else "input.txt"
# input_file = "test.txt"
input_file = "input.txt"

with open(input_file, "r") as f:
    input_values = [n for n in f.read().splitlines()]

# ------------------ #

def partOne():
    aim = 0
    depth = 0
    horizontal_position = 0

    for command in input_values:
        command_parts = command.split(" ")
        distance = int(command_parts[1])
        # print(command_parts)

        match command_parts[0]:
            case "forward":
                horizontal_position += distance
                depth += aim * distance
            case "down":
                aim += distance
            case "up":
                aim -= distance

    return depth * horizontal_position

print(partOne())
