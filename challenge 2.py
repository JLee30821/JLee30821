# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even / odd 
# number react differently when divided by 2?

# Extras:

    # If the number is a multiple of 4, print out a different message.
    # Ask the user for two numbers: one number to check (call it num) 
    #and one number to divide by (check). If check divides evenly into num, 
    # tell that to the user. If not, print a different appropriate message.

number = int(input("Input a number: "))

value = number % 2 # finds if value is even or odd using 1 or 0

if number % 4 == 0: # find if input is a multiple of 4
    print("Your number is a multiple of 4")
elif value == 0: # find if input is even
    print("Your number is even")
else: # input is odd
    print("Your number is odd")