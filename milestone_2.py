import random

word_list = ["apple", "peach", "cumquat", "pineapple", "cranberry"] #list of possible words that can be used

print(word_list)

word = random.choice(word_list) #randomly selects a word from the word list

print(word)

guess = input("Please guess a letter?") #prompts the user for their first guess


if len(guess) == 1 and str.isalpha(guess): #checks the user input is only 1 character and that it is alpabetical
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

print(guess)