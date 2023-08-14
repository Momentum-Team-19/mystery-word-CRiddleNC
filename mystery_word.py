# exactly what it sounds like, to use the random module you have to import it first
import random #for random numbers
from anipage import start_screen # from other file import function
import os # import os to clear terminal screen
import pygame # import music
results = ""


def select_word():  # this function will open a file and return a random word
    with open('test-word.txt', 'r') as file:  # with open is the construct used to open our file "test-word.txt" in read mode as the 'r' shows as a file
        file = file.read()  # reads the contents of the opened file in to its own variable called "file", this puts the outside file in "file" as a single string
    words_list = file.split()  # calling .split() on the file string spits it in to a list of words
    return random.choice(words_list)  # uses the random module imported at the top on our words list, returning that random choice


def display_word_board(word, guessed_letters):  # taking two arguments, 'word' = word to be guessed, 'guessed_letters' = a list of the letters the player has guessed
    chosen_word = ""  # initializing an empty string 'chosen_word' which will eventually represent the word being guessed, with underscores = unguessed letters
    for letter in word:  # starts the for loop that iterates over each letter in 'word' 'word' is what needs to be guessed one by one
        if letter in guessed_letters:  # checking if 'letter' is present in the 'guessed_letters' list
            chosen_word += letter  # if 'letter' is in 'guessed_letters' add it to the 'chosen_word' string
        else:
            chosen_word += "_"  # if the letter is incorrect, add an underscore to the 'chosen_word' string
    return chosen_word  # once every letter has been checked, return the current 'chosen_word' so we can see whats underscores and whats been guessed
    # eventually this function will take in the word and display it as hidden via underscores or letters that have been correctly guessed


def user_guess(counter):  # function to take the user input in the form of a single letter guess
    while counter > 0:  # starts my loop that will go until a break statement or an exception happens
        if counter != 0:  # putting the display for the counter in a loop that runs as long as the player has guesses left
            print(f"You have {counter} guesses left.")  # actually printing the counter message to the screen
            
        # initalize guess as a variable to store the user input and prompts the user to "Guess a letter", .lower() tacked on makes the input come in the desired form - lowercase
        guess = input("Guess a letter: ->").lower().strip()  # strip() to remove all white space
        # double if statment that checks for two conditions, if len(guess) != 1 makes sure the user just entered 
        # or not guess.isalpha() checks the input 'guess' contains any non-alphabet characters
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
        else:  # if it passes then 
            return guess  # returns the users valid guess that gets used later
    # eventually this function will take in user input, check it and return if it was correct or incorrect


def play_game():  # play_game function, holds the game loop and tracks the guessed letters
    os.system('clear')
    global results
    random_word = select_word()  # calls the select_word function to pick a random word and assigns it to the variable 'random_word'    
    guessed_letters = []  # initializing an empty list called 'guessed_letters' - this is a container to store the letters the user has guessed
    counter = 8  # setting counter ammount
    
    while counter > 0:
        display = display_word_board(random_word, guessed_letters)  # calls the display_word_board function with random_word and guessed_letters as arguments, gets the current state of the word fixed with guessed letters and '_' - assigns that to 'display'
        print(display)

        if "_" not in display:  # breaks the loop! checks the updated word for underscores, if there are none then BREAK!
            results = "win"
            os.system('clear')
            start_screen("win")
            print(f"Hey, way to go! You guessed the word! {random_word}")
            break

        guess = user_guess(counter)  # if the word has not been guessed then call 'user_guess' to get a new letter, assigns that to the variable 'guess'
        guessed_letters.append(guess)  # the guessed letter in the 'guess' variable is added to the 'guessed_letters' list to keep track of the guesses so far
        if guess not in random_word:  # adds the count down function inside the game loop 
            counter -= 1
    else:  # else to the while loop, when counter is no longer meeting the condition aka you lost, print the end message
        results = "loss"
        os.system('clear')
        start_screen("loss")
        print(f"Game Over. The word was: {random_word}")
        


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('music/Song1-Motor-Skills-111316.mp3')
    pygame.mixer.music.play(-1)

    replay = True  # setting replay as default true
    start_screen(results)
    play_game()  # first call of the game
    while replay:  # loop determining if you replay
        replay = input("Do you want to play again? (y/n):").lower().strip()  # replay value set by user input
        if replay == "n":
            replay = False
        elif replay == "y":  # if they pick y then we can stay in this loop as long as they like    
            play_game()    
        else:
            print("Choose (y/n)")
    print("Thanks for playing!")
