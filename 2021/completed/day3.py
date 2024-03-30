#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


# input_file = "test.txt" if sys.argv[0] == 1 else "input.txt"
input_file = "day3_test.txt"
input_file = "day3_input.txt"

with open(input_file, "r") as f:
    input_values = [n for n in f.read().splitlines()]

# ------------------ #

# Function calculates the decimal equivalent
# to given binary number
 
def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def partOne():
    
    gamma = ""
    epsilon = ""

    bits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#    bits = [0, 0, 0, 0, 0]

    for line in input_values:
        i = 0
        while i < len(line):
            if int(line[i]) == 1:
                bits[i] += 1
            i += 1

    for bit in bits:
        if bit > (len(input_values) - bit):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

#    print(gamma)
#    print(epsilon)

    gammad = binaryToDecimal(int(gamma))
    epsilond = binaryToDecimal(int(epsilon))

#    print(gammad)
#    print(epsilond)

    return gammad * epsilond

def getMostCommon(report, position):
    bit = 0
    for line in report:
        if int(line[position]) == 1:
            bit += 1
    
    if bit >= (len(report) - bit):
        return 1
    else:
        return 0

def getRating(isFlipped):
    
    i = 0
    length = len(input_values[0])

    currentReport = input_values

    while i < length:
        if len(currentReport) == 1:
            return currentReport[0]
        bit = getMostCommon(currentReport, i)
        bit = 1 - bit if isFlipped else bit
#        print("Most common bit at position " + str(i) + " is " + str(bit))
        newReport = []
        for line in currentReport:
            if bit == int(line[i]):
                newReport.append(line)

        currentReport = newReport
        i += 1


    return currentReport[0]


def partTwo():
    

    oxygen = getRating(False)
    co2 = getRating(True)

    oxygenRating = int(oxygen,2)
    co2Rating = int(co2,2)
#    print("Oxygen Generator Rating in binary: "+oxygen)
#    print("CO2 Scrubber Rating in binary: "+co2)

    return oxygenRating * co2Rating



print("Life support rating of the submarine: " + str(partTwo()))
