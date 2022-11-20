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
import mainframe as mainframe
import admin as admin

choice = ""
user_name = ""
password = ""
isFound = True

while isFound:
    try:
        print("Welcome to the hangman game: \n 1. Start Game \n 2. Show Hi-Score \n 3. Credits \n 4. Login as Admin \n 5. Exit")
        selection = input('>> ')
        selection = int(selection)
        if selection != 5:
            match selection:
                case 1:
                    mainframe.main()
                case 2:
                    mainframe.Hiscore()
                    pass
                case 3:
                    mainframe.Credits(choice)
                case 4:
                    user_name = input("Please enter your name \n >> ")
                    password = input("Please enter your password \n >> ")
                    if user_name == "admin" and password == "qQ1@":
                        admin.Admin_panel()
                    else:
                        print("Username or Password is not valid!\n")

                case 5:
                    print("Exit")
                    break
                case _:
                    print("Please type in a selection within 1 to 4!")
        else:
            break
    except:
        print("Pls enter a number")
