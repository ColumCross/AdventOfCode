#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def partTwo():
    fish = [2,3,1,3,4,4,1,5,2,3,1,1,4,5,5,3,5,5,4,1,2,1,1,1,1,1,1,4,1,1,1,4,1,3,1,4,1,1,4,1,3,4,5,1,1,5,3,4,3,4,1,5,1,3,1,1,1,3,5,3,2,3,1,5,2,2,1,1,4,1,1,2,2,2,2,3,2,1,2,5,4,1,1,1,5,5,3,1,3,2,2,2,5,1,5,2,4,1,1,3,3,5,2,3,1,2,1,5,1,4,3,5,2,1,5,3,4,4,5,3,1,2,4,3,4,1,3,1,1,2,5,4,3,5,3,2,1,4,1,4,4,2,3,1,1,2,1,1,3,3,3,1,1,2,2,1,1,1,5,1,5,1,4,5,1,5,2,4,3,1,1,3,2,2,1,4,3,1,1,1,3,3,3,4,5,2,3,3,1,3,1,4,1,1,1,2,5,1,4,1,2,4,5,4,1,5,1,5,5,1,5,5,2,5,5,1,4,5,1,1,3,2,5,5,5,4,3,2,5,4,1,1,2,4,4,1,1,1,3,2,1,1,2,1,2,2,3,4,5,4,1,4,5,1,1,5,5,1,4,1,4,4,1,5,3,1,4,3,5,3,1,3,1,4,2,4,5,1,4,1,2,4,1,2,5,1,1,5,1,1,3,1,1,2,3,4,2,4,3,1]
    total_fish = 0

    one = populate(1, 0)
    print("1 = " + str(one))
    two = populate(2, 0)
    print("2 = " + str(two))
    three = populate(3, 0)
    print("3 = " + str(three))
    four = populate(4, 0)
    print("4 = " + str(four))
    five = populate(5, 0)
    print("5 = " + str(five))

    for f in fish:
        # total_fish += populate(f, 0)
        # print("Current fish total is: "+str(total_fish))

        match f:
            case 1:
                total_fish += one
            case 2:
                total_fish += two
            case 3:
                total_fish += three
            case 4:
                total_fish += four
            case 5:
                total_fish += five
            case _:
                total_fish += populate(f, 0)

        print("Current fish total is: "+str(total_fish))
            


    print("The answer is: " + str(total_fish))

def populate(fish, day):
    total_fishes = 0
    while day < 256:
        day += 1

        if fish > 0:
            fish -= 1
        else:
            fish = 6
            total_fishes += populate(8, day)

        #print("After day " + str(day) + " the number of fish is: " + str(total_fishes))

    return total_fishes + 1

partTwo()