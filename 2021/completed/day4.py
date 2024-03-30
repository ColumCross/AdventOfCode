#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


input_file = "test.txt" # if sys.argv[1] == 1 else "input.txt"
input_file = "day4_input.txt"

with open(input_file, "r") as f:
    input_values = [n for n in f.read().splitlines()]

# ------------------ #

numbers = input_values[0].split(",")
boards = []

def buildBoard(startIndex, endIndex):
    board = []
    while startIndex < endIndex:
        row = input_values[startIndex].split(" ")
        row = [i for i in row if i != ""]
#        list(filter(lambda a: a != "", row))
        board.append(row)
        startIndex += 1
#    board = [i for i in board if i != " "]
    return board

def partOne():
    i = 2
    while i < len(input_values):
        boards.append(buildBoard(i, i+5))
        i += 6

    for number in numbers:
        b = 0
        while b < len(boards):
            markBoard(number, b)
            if checkBoard(boards[b]):
                print(boards)
                return calculateScore(boards[b]) * int(number)
            b += 1



    print(numbers)
    print(boards)

def markBoard(number, boardIndex):
    r = 0
    while r < 5:
        s = 0
        while s < 5:
            boards[boardIndex][r][s] = "X" if boards[boardIndex][r][s] == number else boards[boardIndex][r][s]
            s += 1
        r += 1

# Python program to get transpose
# elements of two dimension list
def transpose(l1):
 
    # we have nested loops in comprehensions
    # value of i is assigned using inner loop
    # then value of item is directed by row[i]
    # and appended to l2
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2


def checkBoard(board):
    if checkRows(board):
        return True
    else:
        return checkRows(transpose(board))


#   This checks across ones
def checkRows(board):
    for row in board:
        if row == ["X", "X", "X", "X", "X"]:
            return True

    return False

def calculateScore(board):
    score = 0
    for row in board:
        for square in row:
            if square != "X":
                score += int(square)

    return score
    

def partTwo():
    i = 2
    while i < len(input_values):
        boards.append(buildBoard(i, i+5))
        i += 6

    #print(numbers)

    for number in numbers:
        b = 0
        while b < len(boards):
            markBoard(number, b)
            if checkBoard(boards[b]):
                if len(boards) > 1:
                    boards.pop(b)
                    b = -1
                else:
                    print(number)
                    print(boards)
                    return calculateScore(boards[0]) * int(number)
            b += 1
       
#        if len(boards) == 1:
#            print(boards)
#            return calculateScore(boards[0]) * int(number)



#print(partOne())
print(partTwo())
