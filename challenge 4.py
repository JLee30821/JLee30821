user_number = int(input("input a number:"))

user_list = range(1, user_number + 1) # grabs all numbers the user inputted and the numbers less than

output = [] # empty list to append in to

for i in user_list: # loops till i reaches user number plus 1
    if user_number % i == 0: # checks if user number has no remainders
        output.append(i) # appened divisors number in to output list
 
print(output)