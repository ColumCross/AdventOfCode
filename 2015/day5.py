
# Validates if the string is naughty or nice.
# Returns true if nice and false if naughty.
def validateString(inpt):
    # First filter out the guard cases.
    # It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    if("ab" in inpt or "cd" in inpt or "pq" in inpt or "xy" in inpt): return False

    # Loop through the string to check the other two rules.
    # It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    # It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    # Note: I initially thought about using RegEx for at least one of these rules, however if I'm going to be looping throught the string anyway might as well make the best of it.
    number_of_vowels = 0
    contains_double = False
    previous_letter = ""

    for letter in inpt:
        if letter in "aeiou": number_of_vowels += 1
        if letter == previous_letter: contains_double = True
        previous_letter = letter

    if(number_of_vowels >= 3 and contains_double):
        return True
    else:
        return False


input_file = "test.txt"
#input_file = "../inputs/day5input.txt"
f = open(input_file, "r")
input_values = f.readlines()

number_of_nice = 0
for foobar in input_values:
    if validateString(foobar): number_of_nice += 1

print(f"Using part one rules: There are {number_of_nice} nice strings in the list.")

def validateStringPartTwo(inpt):

    rule1 = False
    rule2 = False

    for n in range(0, len(inpt)):
        
        # It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
        try:
            print(inpt[n]+inpt[n+1] + inpt[n+2]+inpt[n+3])
            if inpt[n]+inpt[n+1] == inpt[n+2]+inpt[n+3]: rule1 = True
        except:
            # Index out of range
            pass

        # It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
        try:
            if inpt[n] == inpt[n+2]: rule2 = True
        except Exception as e:
            # Indox out of range
            pass

    return rule1 and rule2

number_of_nice = 0
for foobar in input_values:
    if validateStringPartTwo(foobar): number_of_nice += 1

print(f"Using part two rules: There are {number_of_nice} nice strings in the list.")
