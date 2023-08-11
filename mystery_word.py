# exactly what it sounds like, to use the random module you have to import it first
import random
from anipage import start_screen

# this function will open a file and return a random word
def select_word():
    # with open is the construct used to open our file "test-word.txt" in read mode as the 'r' shows as a file
    with open('test-word.txt', 'r') as file:
        # reads the contents of the opened file in to its own variable called "file", this puts the outside file in "file" as a single string
        file = file.read()
    # calling .split() on the file string spits it in to a list of words
    words_list = file.split()
    # uses the random module imported at the top on our words list, returning that random choice
    return random.choice(words_list)

# taking two arguments, 'word' = word to be guessed, 'guessed_letters' = a list of the letters the player has guessed
def display_word_board(word, guessed_letters):
    # initializing an empty string 'chosen_word' which will eventually represent the word being guessed, with underscores = unguessed letters
    chosen_word = ""
    # starts the for loop that iterates over each letter in 'word' 'word' is what needs to be guessed one by one
    for letter in word:
        # checking if 'letter' is present in the 'guessed_letters' list
        if letter in guessed_letters:
            # if 'letter' is in 'guessed_letters' add it to the 'chosen_word' string
            chosen_word += letter
        else:
            # if the letter is incorrect, add an underscore to the 'chosen_word' string
            chosen_word += "_"
    # once every letter has been checked, return the current 'chosen_word' so we can see whats underscores and whats been guessed
    return chosen_word
    # eventually this function will take in the word and display it as hidden via underscores or letters that have been correctly guessed

# function to take the user input in the form of a single letter guess
def user_guess(counter):
    # starts my loop that will go until a break statement or an exception happens
    while counter > 0:
        # putting the display for the counter in a loop that runs as long as the player has guesses left
        if counter != 0:
            # actually printing the counter message to the screen
            print(f"You have {counter} guesses left.")
            
        # initalize guess as a variable to store the user input and prompts the user to "Guess a letter", .lower() tacked on makes the input come in the desired form - lowercase
        # strip() to remove all white space
        guess = input("Guess a letter: ->").lower().strip()
        # double if statment that checks for two conditions, if len(guess) != 1 makes sure the user just entered 
        # or not guess.isalpha() checks the input 'guess' contains any non-alphabet characters
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
        # if it passes then 
        else:
            # returns the users valid guess that gets used later
            return guess    
    # eventually this function will take in user input, check it and return if it was correct or incorrect


# play_game function, holds the game loop and tracks the guessed letters
def play_game():
    # calls the select_word function to pick a random word and assigns it to the variable 'random_word'
    random_word = select_word()
    # initializing an empty list called 'guessed_letters' - this is a container to store the letters the user has guessed
    guessed_letters = []
    # setting counter ammount
    counter = 8
        # starts the loop, its infinate until it hits 'break' or an exception occurs. This is the game logic itself
    while counter > 0:
        # calls the display_word_board function with random_word and guessed_letters as arguments
        # gets the current state of the word fixed with guessed letters and '_' - assigns that to 'display'
        display = display_word_board(random_word, guessed_letters)
        print(display)

        # breaks the loop! checks the updated word for underscores, if there are none then BREAK!
        if "_" not in display:
            start_screen()
            print(f"Hey, way to go! You guessed the word! {random_word}")
            break

        # if the word has not been guessed then call 'user_guess' to get a new letter, assigns that to the variable 'guess'
        guess = user_guess(counter)
        # the guessed letter in the 'guess' variable is added to the 'guessed_letters' list to keep track of the guesses so far
        guessed_letters.append(guess)
        # adds the count down function inside the game loop 
        if guess not in random_word:
            counter -= 1
    # else to the while loop, when counter is no longer meeting the condition aka you lost, print the end message
    else:
        start_screen()
        print(f"Game Over. The word was: {random_word}")
        

if __name__ == "__main__":
    # setting replay as default true
    replay = True
    # first call of the game
    play_game()
    # loop determining if you replay
    while replay:
        # replay value set by user input
        replay = input("Do you want to play again? (y/n):").lower().strip()
        if replay == "n":
            replay = False
        # if they pick y then we can stay in this loop as long as they like    
        elif replay == "y":
            play_game()    
        else:
            print("Choose (y/n)")
    print("Thanks for playing!")