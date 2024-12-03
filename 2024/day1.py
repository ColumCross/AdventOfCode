#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


input_file = "test.txt"
input_file = "input.txt"

left_list = []
right_list = []

with open(input_file, "r") as f:
    for n in f.read().splitlines():
        line = n.split("   ")
        left_list.append(line[0])
        right_list.append(line[1])

left_list.sort()
right_list.sort()

part1_ans = 0
i = 0;
while i < len(left_list):
    part1_ans += abs(int(right_list[i]) - int(left_list[i]))
    i += 1

print("Part One Answer:")
print(part1_ans)
print("-----")

part2_ans = 0
for location in left_list:
    part2_ans += int(location) * len([x for x in right_list if x == location])


print("Part Two Answer:")
print(part2_ans)
print("-----")
