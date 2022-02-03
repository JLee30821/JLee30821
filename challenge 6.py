print("This program will tell you if your word is a palindrome or not")

user_input = input("Please type out a word: ")

if user_input == user_input[::-1]: 
    print ("Yas Palindrome")
else:
    print("nah thats ugly")
    
# what [::-1] does in this code is it grabs the user's input and reverses
# it. Then the program compares it to the original input to see if they 
# match. If they match the program spits out yas palindrome
    