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
# import pandas as pd
from Animals import word_list_animals_easy
from Animals import word_list_animals_medium
from Animals import word_list_animals_hard
#Allow for user input

difficulty_settings = "" #Allows selection of difficulty   input("Please enter a difficulty:\n 1. Easy\n 2. Medium\n 3. Hard\n > ")
players = "" #Allows user to key in amount of players
username = "" #Input player's name
userKeyed = ""#input("Select a valid character [a-z,']: ") #logs what user has typed in
options = ""#input("")
regexstr = "/^[a-zA-Z]+$/"

# def StartGame(players_no, player_name, chosen_difficulty):
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
    word = random.choice(word_list_animals_easy)
    return word.upper()

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

def player_count():
    return

def Hiscore():
    print("Hi-scores of other players: ")
    
def Credits(Cont): 
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
    pass
    Cont = input("Enter [Y]es to see page 2 or [N] to stop: ")
    
    if Cont == "Y":
        print(".-=~=-.                                                                 .-=~=-.")
        print("(__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)")
        print("( _ __) Property of FlufCorp  Property of FlufCorp  Property of FlufCorp( _ __)")
        print("(__  _)                                                                 (__  _)")
        print("(_ ___)                ♥Welcome to the credits page 2♥                  (_ ___)")
        print("(__  _)                             Socials                             (__  _)")
        print("( _ __)    Github: https://github.com/TheOneFluffer?tab=repositories    ( _ __)")
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
        return

    elif Cont == "N":
        return

    else:
        print("Please type in Y to continue or N to stop")
        pass

# def Exit():
    