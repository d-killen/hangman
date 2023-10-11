import random

class Hangman:

    #init method
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list) # selects a word randomly from the passed list
        self.word_guessed = ["_" for x in self.word] # _ for each letter not yet guessed; e.g. for pear ['_','_','_','_',]
        self.num_letters = len(set(self.word)) #number of unique letters in the word
        self.num_lives = num_lives #number of lives at start of game, default is 5
        self.word_list = word_list #list of words
        self.list_of_guesses = [] #list of guesses already made

    #this method checks whether the users guess is in the chosen word
    def check_guess(self, guess):
        guess = guess.lower() #converts the input to lower case
    
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index]=letter #adds the guess in position to the word_guessed list
            self.num_letters -= 1 #reduces unique letters remaining
        else:
            self.num_lives -= 1 #reduces lives left
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")
        return
    
    #this method prompts the user for a guess and checks it is a valid guess     
    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter:") #prompts the user for their guess

            if len(guess) != 1 or str.isalpha(guess) == False: #checks the user input is only 1 character and that it is alpabetical
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: #checks if already guessed
                print("You already tried that letter!")
            else:
                self.check_guess(guess) #checks if the guess is in the word
                self.list_of_guesses.append(guess) #adds the guess to the list of guesses

