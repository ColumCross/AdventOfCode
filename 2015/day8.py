
#input_file = "test.txt"
input_file = "../inputs/day8_input.txt"
f = open(input_file, "r")
input_values = f.read()
input_values = input_values.splitlines()

#print(input_values)

total_string = 0
total_memory = 0
total_new_string = 0

for strong in input_values:
    
    single_string = 0
    single_memory = 0
    new_string = 2

    n = 0
    while n < len(strong):
        if strong[n] == "\\":
            match strong[n+1]:
                case '\\':
                    single_memory += 1
                    new_string += 4
                    n += 2
                case '"':
                    single_memory += 1
                    new_string += 4
                    n += 2
                case 'x':
                    single_memory += 1
                    new_string += 5
                    n += 4
                case _:
                    raise Exception(strong[n+1])
        elif strong[n] == '"':
            new_string += 2
            n += 1
        else:
            single_memory += 1
            new_string += 1
            n += 1

    #print(str(len(strong)) + " & " + str(single_memory))
    #print(new_string)

    total_string += len(strong)
    total_memory += single_memory
    total_new_string += new_string

print("Total number of characters: ", end="")
print(total_string)
print("Total number in memory: ", end="")
print(total_memory)
print("Answer to part 1: ", end="")
print(total_string - total_memory)
print("Answer to part 2: ", end="")
print(total_new_string - total_string)
