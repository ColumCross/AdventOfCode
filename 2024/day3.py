#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

input_file = "test.txt"
input_file = "input.txt"

with open(input_file, "r") as f:
    str = f.read()

#Regex
# /mul\(\d+,\d+\)/gm
# mul\(\d+,\d+\)|don't\(\)|do\(\)
match = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", str)

calc = True
p1ans = 0
p2ans = 0

for exp in match:
    if(exp[0] == "m"):
        items = re.findall(r"\d+", exp)
        ans = int(items[0]) * int(items[1])
        p1ans += ans
        if calc:
            p2ans += ans
    elif exp == "do()":
        calc = True
    elif exp == "don't()":
        calc = False
    else:
        raise Exception("Bad exp")


print("Part One Answer:")
print(p1ans)
print("-----")
print("Part Two Answer:")
print(p2ans)
print("-----")