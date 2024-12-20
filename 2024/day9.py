#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input = ""

p1ans = 0
p2ans = 0

# loop through the input
# mod the input on the index
# if it's odd:
    # add the current file id the number times to the major list
    # increment the thing

bitIndex = 1 # Starting the index at 1 because I'm CRAZY
fileID = 0
expandedDisk = []

for bit in input:
    if bitIndex % 2 == 0:
        for x in range(0,int(bit)):
            expandedDisk.append(".")
    else:
        for x in range(0, int(bit)):
            expandedDisk.append(fileID)
        fileID += 1
    bitIndex += 1

p2Disk = expandedDisk.copy()

while "." in expandedDisk:
    try:
        expandedDisk[expandedDisk.index(".")] = expandedDisk.pop()
    except:
        break

for i in range(0, len(expandedDisk)):
    p1ans += i * expandedDisk[i]

print("Part One Answer:")
print(p1ans)
print("-----")





print("Part Two Answer:")
print(p2ans)
print("-----")