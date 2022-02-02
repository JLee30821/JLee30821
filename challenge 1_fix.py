# Challange 1

name = input("What is your name?: ") 

age = int(input("WHat is your age?: "))

repeat = int(input("How many times should we repeat?: "))

old_age = 100 - age # to find age till they are age 100

year = (2022 - age) + 100 # to find what year they will be age 100

for i in range(repeat): # to loop as many times as the user wanted the print to be printed
    print(name, "you will be 100 years old in", old_age, "years or in", year)
    