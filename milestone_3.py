
#this functions prompts the user for a guess and checks it is a valid guess     
def ask_for_input():
    while True:
        guess = input("Please guess a letter:") #prompts the user for their guess

        if len(guess) == 1 and str.isalpha(guess): #checks the user input is only 1 character and that it is alpabetical
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess) #checks if the guess is in the word

    return

#this function checks whether the users guess is in the chosen word
def check_guess(guess):
    guess = guess.lower() #converts the input to lower case
    
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try Again.")
    return

secret_word = "test"
ask_for_input()