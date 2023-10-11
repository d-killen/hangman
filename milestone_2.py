import random

word_list = ["apple", "peach", "cumquat", "pineapple", "cranberry"]

print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Please guess a letter?")

if len(guess) == 1 and str.isalpha(guess):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

print(guess)
