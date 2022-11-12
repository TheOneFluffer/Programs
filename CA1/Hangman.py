
"""
Main program

Student ID: p2241319
Name: Lau Hong Wei
Class: DISM/FT/1B/08
Assessment: CA1-1

Script name:
    CA1-Hangman.py
Purpose:
    Purpose of this script is for users to choose from choices 1 to 4 and it will run appropriate 

Usage syntax:
    Run with play button / command line, e.g. py Hangman.py

Input file:

Output file:

Python version:
Python 3

Features needed:
    Player name:
    Secret word:
    Game word:
    Score
    Top X players
    Game log
"""

#User selection screen
import admin as admin

selection = ""
choice = ""
isFound = True

while isFound:
    try:
        print("Welcome to the hangman game: \n 1. Start Game \n 2. Show Hi-Score \n 3. Credits \n 4. Exit")
        selection = input('Enter choice: ')
        selection = int(selection)
        if selection != 4:
            match selection:
                case 1:
                    # StartGame(players, username, difficulty_settings)
                    pass
                case 2:
                    print("Hello")
                case 3:
                    admin.Credits(choice)
                    pass
                    # print("Star walkinnn")
                case 4:
                    print("Exit")
                case _:
                    print("Please type in a selection within 1 to 4!")
        else:
            break
    except:
        print("Pls enter a number")