#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# input_file = "test.txt"

# with open(input_file, "r") as f:
#     input_values = [n for n in f.read().split(",")]

from math import floor


input = "2,3,1,3,4,4,1,5,2,3,1,1,4,5,5,3,5,5,4,1,2,1,1,1,1,1,1,4,1,1,1,4,1,3,1,4,1,1,4,1,3,4,5,1,1,5,3,4,3,4,1,5,1,3,1,1,1,3,5,3,2,3,1,5,2,2,1,1,4,1,1,2,2,2,2,3,2,1,2,5,4,1,1,1,5,5,3,1,3,2,2,2,5,1,5,2,4,1,1,3,3,5,2,3,1,2,1,5,1,4,3,5,2,1,5,3,4,4,5,3,1,2,4,3,4,1,3,1,1,2,5,4,3,5,3,2,1,4,1,4,4,2,3,1,1,2,1,1,3,3,3,1,1,2,2,1,1,1,5,1,5,1,4,5,1,5,2,4,3,1,1,3,2,2,1,4,3,1,1,1,3,3,3,4,5,2,3,3,1,3,1,4,1,1,1,2,5,1,4,1,2,4,5,4,1,5,1,5,5,1,5,5,2,5,5,1,4,5,1,1,3,2,5,5,5,4,3,2,5,4,1,1,2,4,4,1,1,1,3,2,1,1,2,1,2,2,3,4,5,4,1,4,5,1,1,5,5,1,4,1,4,4,1,5,3,1,4,3,5,3,1,3,1,4,2,4,5,1,4,1,2,4,1,2,5,1,1,5,1,1,3,1,1,2,3,4,2,4,3,1"
input_values = [n for n in input.split(",")]

# ------------------ #

class LanternFish:

    def __init__(self, age):
        self.age = age

    def newDay(self):
        if self.age > 0:
            self.age -= 1
            return False
        else:
            self.age = 6
            return LanternFish(8)

    def __str__(self) -> str:
        return str(self.age)

def populate(days, fish):
    day = 0
    while day < days:
        newFishes = []
        dailyMessage = "After day " + str(day+1) + ": "
        for lanternFish in fish:
            newFish = lanternFish.newDay()
            # dailyMessage += str(lanternFish) + ","
            if newFish:
                newFishes.append(newFish)
                # dailyMessage += str(newFish) + ","

        fish.extend(newFishes)

        dailyMessage += str(len(fish))
        print(dailyMessage)
        day += 1

    return len(fish)

def partOne():
    # print("Initial State: " + str(input_values))
    totalFish = populate(80, [LanternFish(int(line)) for line in input_values])
    print("The answer is: " + str(totalFish))

# partOne()

def partTwo():
    # print("Initial State: " + str(input_values))
    days = 256
    fish = [int(line) for line in input_values]
#    fish = [3,4,3,1,2]
    total_fish = 0
    for f in fish:
        # total_fish += populate(days, [LanternFish(f)])
        total_fish += newPopulate(f, days)
        print("Current fish total is: "+str(total_fish))


    print("The answer is: " + str(total_fish))

def makeFish(gestation):
    return    

def newPopulate(firstFish, days):
    fish = [firstFish]
    day = 0
    while day < days:
        newFishes = []
        for lanternFish in fish:
            if lanternFish > 0:
                lanternFish -= 1
                newFishes.append(lanternFish)
            else:
                newFishes.append(6)
                newFishes.append(8)

        fish = newFishes
        day += 1
        print("After day " + str(day) + " the number of fish is: " + str(len(fish)))

    return len(fish)

def answer(days, fish):
    total_fish = 0

    while days > 0:
        days -= fish
        total_fish


#partOne()
partTwo()    
