def calculateBox(l, w, h):

    # Calculate SA
    sa = 2*l*w + 2*w*h + 2*h*l

    # Calculate area of the smallest side
    sides = [l*w, l*h, w*h]
    sides.sort()
    smallestSide = sides[0]

    return sa + smallestSide

def calculateRibbon(l, w, h):
    bow = l*w*h

    sides = [l,w,h]
    sides.sort()
    ribbon = 2*sides[0] + 2*sides[1]

    return ribbon+bow

# input_file = "test.txt"
input_file = "../inputs/2input1.txt"
total_amount = 0
ribbon_amount = 0


f = open(input_file, "r")
input_values = f.readlines()


for dimension in input_values:
    dimension = dimension.strip("\n")
    dimensions = dimension.split("x")


    total_amount += calculateBox(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))
    ribbon_amount += calculateRibbon(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))

print("Final Amount Needed:")
print(total_amount)
print("Ribbon Length Needed:")
print(ribbon_amount)
