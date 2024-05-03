from collections import defaultdict

#input_file = "test.txt"
input_file = "../inputs/3input1.txt"
f = open(input_file, "r")
input_values = f.read()

def generateHousemap():
    housemap = {}
    housemap["0,0"] = 0

    return housemap

def deliverPresents(directionlist, housemap):


    x = 0
    y = 0

    housemap["0,0"] += 1

    for direction in directionlist:
        match direction:
            case "^":
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1
            case _:
                continue

        coords = str(x) + "," + str(y)

        try:
            housemap[coords] += 1

        except:
            housemap[coords] = 1

    return housemap

def calculateHouses(housemap):

    numberOfHouses = 0
    doubledHouses = 0

    for house in housemap:
        numberOfHouses += 1
        if housemap[house] > 1:
            doubledHouses += 1

    return numberOfHouses

partOne = calculateHouses(deliverPresents(input_values, generateHousemap()))
print("Santa alone delivered to this many houses:")
print(partOne)

santasInstructions = ""
robotsInstructions = ""
for i in range(0, len(input_values)):
    if i%2==0:
        santasInstructions += input_values[i]
    else:
        robotsInstructions += input_values[i]

santHouses = deliverPresents(santasInstructions, generateHousemap())
robotHouses = deliverPresents(robotsInstructions, santHouses)
print("Santa and the robot delivered to this many houses:")
print(calculateHouses(robotHouses))
