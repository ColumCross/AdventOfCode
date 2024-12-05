# Python 3 code to demonstrate the 
# working of MD5 (string - hexadecimal)
 
import hashlib
 

def hashstring(str2hash):

# encoding GeeksforGeeks using encode()
# then sending to md5()
    result = hashlib.md5(str2hash.encode())
     
    return result.hexdigest()

base_input = "yzbqklnj"
current_hash = ""
incrementer = -1 # Start one below becuase incrementer must incrementer first.

# Part 1, 5 0s
while(current_hash[0:5:1] != "00000"):
    incrementer += 1
    current_hash = hashstring(base_input + str(incrementer))

print("The answer to part one is: ", end ="")
print(incrementer)

# Part 2, 6 0s
incrementer = 198570000000 # Last value attained during one test
while(current_hash[0:5:1] != "000000"):
    
    incrementer += 1
    # Print the current incrementer so I know where I am. Helps to see the program still running becuase I don't care about time efficiency.
    # Only print every 1000000 iterations because the act of printing takes longer than the rest of the code per cycle.
    if(incrementer%1000000==0): print("Still calculating final result. Currently at: "+str(incrementer), end='\r')
    
    current_hash = hashstring(base_input + str(incrementer))

print("The answer to part two is: ", end ="")
print(incrementer)
