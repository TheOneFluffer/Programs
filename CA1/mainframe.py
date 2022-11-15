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
import datetime
# import json
from word_list import existing_words, new_words
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

def get_wordndef():
    total_words = existing_words + new_words
    category_key = list((total_words.keys())) #simple is a dictionary
    word = (random.randint(0, len(category_key) - 1)) #generate random word
    rand_word = category_key[word]
    rand_def = total_words[rand_word]
    return rand_word.lower(), rand_def.lower()

def play(word, username, rand_word, rand_def):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 5
    points = 0
    print("H A N G M A N\n")
    print("Player:",username)
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter: {guess}")
            elif guess not in word:
                print(f"{guess}, is not in the word!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Nice, {guess}, is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indexes = [i for i, letter in enumerate(word) if letter == guess]
                points += 2

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
            else:
                guess = True
                word_completion = word

        else:
            print("Not a valid guess")

        print(display_hangman(tries))
        print("Used letters: "," ".join(guessed_letters), "(",len(guessed_letters),")" )
        print("\n")
        print(word_completion)
        print("\n")
    if guessed:
        print(word, end=": ")# Print the key
        print(f"Congratulations, You win! The secret word is {rand_word}: {rand_def}")
    else:
        print("Maximum number of guesses!")
        print(f"After 5 incorrect guesses, The word was {rand_word}: {rand_def}")
    return points

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
    rand_word,rand_def = get_wordndef()
    username = input("Please enter name: ")
    play(rand_word, username, rand_word, rand_def)
    while input("Enter [Y]es to play again or [N] to quit: ").lower() == "y":
        rand_word,rand_def = get_wordndef()
        play(rand_word, username, rand_word, rand_def)

if __name__ == "__main__":
    main()

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