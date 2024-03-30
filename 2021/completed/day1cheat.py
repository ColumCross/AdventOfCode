#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt", "r") as f:
    input_values = [int(n) for n in f.read().splitlines()]

# ------------------ #

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
