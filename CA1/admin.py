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

isFound = True

def Admin_panel():
    while isFound:
        try:
            print("Welcome to the admin panel: \n 1. Add word \n 2. Delete word \n 3. Edit word \n 4. View logs \n 5. Exit")
            selection = input('Enter choice: ')
            selection = int(selection)
            if selection != 5:
                match selection:
                    case 1:
                        pass
                    case 2:
                        # mainframe.Hiscore()
                        pass
                    case 3:
                        pass
                    case 4:
                        print("Men")
                    case 5:
                        print("Exit")
                    case _:
                        print("Please type in a selection within 1 to 4!")
            else:
                break
        except:
            print("Pls enter a number")