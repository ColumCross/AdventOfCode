#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt", "r") as f:
    input_values = [int(n) for n in f.read().splitlines()]

# ------------------ #

lines = []
x = 2

while x < len(input_values):
	sum = input_values[x-2] + input_values[x-1] + input_values[x]
	lines.append(sum)
	x += 1





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
