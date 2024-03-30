#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_file = "test.txt"
input_file = "day8_input.txt"

with open(input_file, "r") as f:
    input_values = [n for n in f.read().splitlines()]

input_values = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]

def partOne():
    output_values = []
    for pattern in input_values:
        output = pattern.split(" | ")[1]
        output_values.extend(output.split(" "))

    unique_values = 0
    for digit in output_values:
        if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
            unique_values += 1

    return unique_values

# go through the lines, determine the mapping and decode them.
def partTwo():
    total_value = 0
    for line in input_values:
        inputs = line.split(" | ")[0].split(" ")
        # print(str(inputs))
        determineMapping(inputs)

    return

# 
def determineMapping(input):

    one = ""
    four = ""
    seven = ""
    eight = ""

    for pattern in input:
        match len(pattern):
            case 2:
                one = set(pattern)
            case 4:
                four = set(pattern)
            case 3:
                seven = set(pattern)
            case 7:
                eight = set(pattern)

    # print(str(seven))
    # What 7 has, but 1 doesn't is A
    # mapping["a"] = one.symmetric_difference(seven)
    a = one.symmetric_difference(seven)

    # 4 + A = 9 - G
    # G = 9 - 4 - A
    # 9 is a 6 segment that is 4andA with only one extra. That one extra is G
    fouranda = set.union(four, a)
    for pattern in input:
        if len(pattern) != 6:
            continue
        diff = fouranda.symmetric_difference(set(pattern))
        if len(diff) == 1:
            g = list(diff)[0]

    # E = 8 - 4 - A - G
    e = eight.symmetric_difference(set.union(fouranda, set(g)))

    mapping = {
        list(a)[0]: "a",
        # "b",
        # "c",
        # "d",
        list(e)[0]: "e",
        # "f",
        g: "g"
    }

    print(str(mapping))

    return

def decodeOutput(outputValues, mapping):
    return

# print("Answer to part one: " + str(partOne()))
partTwo()