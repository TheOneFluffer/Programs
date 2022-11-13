"""
Main program

Student ID: p2241319
Name: Lau Hong Wei
Class: DISM/FT/1B/08
Assessment: CA1-1

Script name:
    CA1-Hangman.py
Purpose:
    Purpose of this script is for the hangman script to run properly as this will be imported from the client side

Usage syntax:
    Run with play button / command line, e.g. py Hangman.py

Input file:

Output file:

Python version:
Python 3

Features needed:
    Access control:
    Add, delete or edit:
    Report:

Credit:
    https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c Hangman ASCII github
    https://www.youtube.com/watch?v=m4nEnsavl6w Hangman Tutorial
"""

#importing stuff
import random
import re
from word_list import simple_words
from word_list_advanced import advanced_words
#Allow for user input

# def StartGame(players_no, player_name, chosen_difficulty):
    # difficulty_settings = "" #Allows selection of difficulty   input("Please enter a difficulty:\n 1. Simple\n 2. Advanced\n > ")
    # players = "" #Allows user to key in amount of players
    # username = "" #Input player's name
    # #logs what user has typed in
    # options = ""
# regexstr = "/^[a-zA-Z]+$/"
#     while players_no < 1 and players_no == 0:
#         try:
#             players_no = input("Please enter the amount of players: ")
#             match players_no:
#                 case 1:
#                     username

#                     except:
#                         print("Please enter a name")

#         except:
#             print("Pls enter a number")

def get_word():
    word = random.choice(wordlist) #adding all the wordlists into 1 variable 
    return word.lower()

def play(word):
    word_completion = "_" * len(word)
    guessed = False #If guessed is false, it will keep asking for input
    guessed_letters = [] #Stores what the user has guessed
    wrong_letters = []
    guessed_words = []
    tries = 6
    points = 0

    print("H A N G M A N")
    username = input("Please enter name: ")
    print("Player:",username)
    print(display_hangman(tries))
    # print("Incorrect letters: ", " ".join(wrong_letters), "(",len(wrong_letters),")" )
    print("\n")
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Select a valid character [a-z]: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter: {guess}")

            elif guess not in word:
                print(f"{guess} is not in the word!")
                tries -= 1
                guessed_letters.append(guess)
                wrong_letters = guessed_letters
                print("Guessed letters: ", wrong_letters, "(",len(wrong_letters),")" )

            else:
                print(f"Nice, {guess}, is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indexes = [i for i, letter in enumerate(word) if letter == guess]

                for index in indexes:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word: {guess}")

            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
                wrong_letters = guessed_words
                wrong_letters = " ".join(wrong_letters)

            else:
                guess = True
                word_completion = word

        else:
            print("Not a valid guess")

        print("Player:",username)
        print(display_hangman(tries))
        print("Incorrect letters: "," ".join(wrong_letters), "(",len(wrong_letters),")" )
        print("\n")
        print(word_completion)
        print("\n")
        
    if guessed:
        print(f"Congratulations, The secret word is {word}. You win")

    else:
        print("Maximum number of guesses!")
        # print("After", guessed_words" incorrect guesses and "guessed_letters" correct guess(es), the word was "word": Description here")
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")
        print("*****")

def display_hangman(tries):
    stages = [  """
         _____
         |    |
         |    O
         |   /|\\
         |   / \\
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |    O
         |   /|\\
         |   / 
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |    O
         |   /|\\
         |   
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |    O
         |   /| 
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |    O
         |    | 
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |    O
         |    
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |    
         |    
         |
        _|_
       |   |________
       |            |
       |____________|
         """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Enter [Y]es to play again or [N] to quit: ").lower() == "y":
        word = get_word()
        play(word)

def player_count():
    return

def Hiscore():

    print("Hi-scores of other players: ")
    
def Credits(Cont):
    print("\n")
    print(".-=~=-.                                                                 .-=~=-.")
    print("(__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)")
    print("( _ __) Property of FlufCorp  Property of FlufCorp  Property of FlufCorp( _ __)")
    print("(__  _)                                                                 (__  _)")
    print("(_ ___)                 ♥Welcome to the credits page 1♥                 (_ ___)")
    print("(__  _)                    This segment is made by                      (__  _)")
    print("( _ __)                   Hong Wei from DISM/FT/1B/08                   ( _ __)")
    print("(__  _)                   CEO of FlufCorp Pte Ltd 2022                  (__  _)")
    print("(_ ___)   I will like to take my time to thank the reader for finding   (_ ___)")
    print("(__  _)            and a big shoutout to Mr Lim for all the             (__  _)")
    print("( _ __)    help that I received during these lessons during the past    ( _ __)")
    print("(__  _)                    few lessons. Therefore...                    (__  _)")
    print("(_ ___)                                                                 (_ ___)")
    print("(__  _)                                                                 (__  _)")
    print("( _ __)                                                                 ( _ __)")
    print("(__  _)                                                                 (__  _)")
    print("(_ ___)                     Thank you for reading!!                     (_ ___)")
    print("(__  _)         From the up and coming ethical hacker/programmer        (__  _)")
    print("( _ __)                                                                 ( _ __)")
    print("(__  _)                                                                 (__  _)")
    print("( _ __)                                                                 ( _ __)")
    print("(__  _) Property of FlufCorp  Property of FlufCorp  Property of FlufCorp(__  _)")
    print("(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)")
    print("`-._.-'                                                                 `-._.-'")
    print("\n")
    pass
    Cont = input("Enter [Y]es to see page 2 or [N] to stop: ").upper()
    
    if Cont == "Y":
        print("\n")
        print(".-=~=-.                                                                 .-=~=-.")
        print("(__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)")
        print("( _ __) Property of FlufCorp  Property of FlufCorp  Property of FlufCorp( _ __)")
        print("(__  _)                                                                 (__  _)")
        print("(_ ___)                ♥Welcome to the credits page 2♥                  (_ ___)")
        print("(__  _)                             Socials                             (__  _)")
        print("( _ __)            Github: https://github.com/TheOneFluffer             ( _ __)")
        print("(__  _)                                                                 (__  _)")
        print("(_ ___)  Linkedin: https://www.linkedin.com/in/lau-hong-wei-966b43247/  (_ ___)")
        print("(__  _)                                                                 (__  _)")
        print("( _ __)       Instagram: https://www.instagram.com/sir_fluffbuns/       ( _ __)")
        print("(__  _)                                                                 (__  _)")
        print("(_ ___)                    Were you expecting more?                     (_ ___)")
        print("(__  _)                                                                 (__  _)")
        print("( _ __)                                                                 ( _ __)")
        print("(__  _)                                                                 (__  _)")
        print("(_ ___)                        That's all folks!!                       (_ ___)")
        print("(__  _)         From the up and coming ethical hacker/programmer        (__  _)")
        print("( _ __)                                                                 ( _ __)")
        print("(__  _)                                                                 (__  _)")
        print("( _ __)                                                                 ( _ __)")
        print("(__  _) Property of FlufCorp  Property of FlufCorp  Property of FlufCorp(__  _)")
        print("(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)")
        print("`-._.-'                                                                 `-._.-'")
        print("\n")
        return

    elif Cont == "N":
        return

    else:
        print("Please type in Y to continue or N to stop")
        pass