# part 1 and 2
a = [1, 1, 25, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print([x for x in a if x < 5]) # picks and prints numbers that are less than 5

# part 3
user = int(input("please enter a number: "))

print([x for x in a if x < user]) # picks and prints numbers that are less than user's number