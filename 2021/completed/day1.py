#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input = open("/home/colum/Documents/AdventOfCode/input.txt")
# input = open("/home/colum/Documents/AdventOfCode/test.txt")
lines = input.read().splitlines()
# print(lines)
increases = 0
decreases = 0
i = 0

while i < len(lines):
	if lines[i] > lines[i-1]:
		increases += 1
	else:
		decreases += 1
	i += 1

print(increases)
print(decreases)
