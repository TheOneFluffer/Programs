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
    https://www.digitalocean.com/community/tutorials/python-add-to-dictionary Adding new words in dictionary
    https://www.youtube.com/watch?v=jaNMhV_NhZE Adding new words in dictionary
"""

#importing stuff
import random
import re
import datetime
import json
from word_list import words
#from Scoreboard import Player_data
#functions are stored in the mainframe.py file. This file is called by both Hangman.py and admin.py
#difficulty is based on how much lives you have, Easy = 10, Normal = 5, Hard = 3

def get_wordndef():
    """
        get_wordndef: getting word and definition from wordlist
        returns: random word and random definition in lowercase 
    """
    total_words = words
    category_key = list((total_words.keys())) #simple is a dictionary
    word = (random.randint(0, len(category_key) - 1)) #generate random word
    rand_word = category_key[word]
    rand_def = total_words[rand_word]
    return rand_word.lower(), rand_def.lower()

def play(word, reduce_by, username, rand_def):
    """
        play: launch hangman game
        Arguements:
            word: get word from dictionary
            username: get user's name for highscore purposes
            rand_word: get word from previous function
            rand_def: get definition from previous function
        returns: Username, score
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 10
    points = 0
    print("H A N G M A N\n")
    print("Player:",username)
    print(display_hangman_template(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter: {guess}")
            elif guess not in word:
                print(f"{guess}, is not in the word!")
                tries -= reduce_by
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
                tries -= reduce_by
                guessed_words.append(guess)
            else:
                guess = True
                word_completion = word

        else:
            print("Not a valid guess")
        print(display_hangman_template(tries))
        print("Used letters: "," ".join(guessed_letters), "(",len(guessed_letters),")" )
        print("\n")
        print(word_completion)
        print("\n")

    if guessed:
        print(word, end=": ")# Print the key
        print(f"Congratulations, You win! The secret word is {word}: {rand_def}")

    else:
        print("Maximum number of guesses!")
        if reduce_by == 1:
            print(f"After 10 incorrect guesses, The word was {word}: {rand_def}")
        else:
            print(f"After 5 incorrect guesses, The word was {word}: {rand_def}")

    if points < 15:
        print("You lose")
    else:
        print
    return points, username

def display_hangman_template(tries):
    stages = [  """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |   / \\
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |   / 
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|\\
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
         |   [O]
         |   /|\\
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
         |   [O]
         |   /|
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
         |   [O]
         |    | 
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
         |   [O]
         |    
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
         |   [O
         |     
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
         |    O
         |     
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
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    
         |    
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

def difficulty():
    reduce_by = 0
    difficulty_settings = int(input("Please select difficulty level:\n [1] Easy\n [2] Standard\n> ")) #Allows selection of difficulty
    if difficulty_settings == 1:
        reduce_by = 1
    elif difficulty_settings == 2:
        reduce_by = 2
    return reduce_by

def main():
    rand_word,rand_def = get_wordndef()
    username = input("Please enter name: ")
    reduce_by = difficulty()
    play(rand_word, reduce_by, username, rand_def)
    while input("Enter [Y]es to play again or [N] to quit: ").lower() == "y":
        rand_word,rand_def = get_wordndef()
        play(rand_word, reduce_by, username, rand_def)

def Hiscore():
    print("Hi-scores of other players: ")
    f = open("I:\Year 1 Sem 2\PSEC\Programs\CA1\Highscore.txt", "r") #To fix this, replace it with your own path
    print(f.read())

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
