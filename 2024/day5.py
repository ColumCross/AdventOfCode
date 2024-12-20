#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random

input_file = "test.txt"
input_file = "input.txt"

fileStart = True

rules = []
updates = []

p1ans = 0
p2ans = 0

def getMiddlePageNumber(update):
    elem = int(len(update)/2)
    return int(update[elem])

def checkRule(rule, update):
    if rule[0] not in update or rule[1] not in update:
        return True
    else:
        if update.index(rule[0]) < update.index(rule[1]):
            return True
        else:
            return False

# def fixUpdate(ruleIndexes, update):
#     # For each rule 

def fixUpdate(update):
    X = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    Y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

    Z = [x for _,x in sorted(zip(Y,X))]
    print(Z)  # ["a", "d", "h", "b", "c", "e", "i", "f", "g"]

with open(input_file, "r") as f:
    for n in f.read().splitlines():
        if(n == ""):
            fileStart = False
            continue

        # Set up the rules
        if fileStart:
            rule = n.split("|")
            rules.append(rule)

        else:
            updates.append(n.split(","))        

# Loop through the updates
for update in updates:
    # For each update check if each rule works
    # Add the result to an array
    answers = []
    for rule in rules:
        answers.append(checkRule(rule, update))
    
    # If every result in the array is True, add the middle page number
    if all(answers):
        p1ans += getMiddlePageNumber(update)
    else:
        print(answers.count(False))
        #print(rules[answers.index(False)])
        #p2ans += tryAgain(update)

print("Part One Answer:")
print(p1ans)
print("-----")
print("Part Two Answer:")
print(p2ans)
print("-----")