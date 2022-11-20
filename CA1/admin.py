"""
Main program

Student ID: p2241319
Name: Lau Hong Wei
Class: DISM/FT/1B/08
Assessment: CA1-1

Script name:
    admin.py
Purpose:
    Purpose of this script is for the admin part of hangman script to run properly as this will be imported from the client side

Usage syntax:
    Run with play button / command line, e.g. py Hangman.py

Input file:

Output file:

Python version:
Python 3

Features needed:
    Access control:
    Add, delete or edit:
    Editing settings as well
    Report:

Credit:
    https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c Hangman ASCII github
    https://www.youtube.com/watch?v=m4nEnsavl6w Hangman Tutorial
"""

#importing stuff
import mainframe_admin as mainframe
from word_list import words
isFound = True

def menu():
    print("Welcome to the admin panel: \n 1. Add word \n 2. Delete word \n 3. Edit word \n 4. View logs \n 5. Exit")
    selection = input('Enter choice: ')
    return selection

def check_word(checkWord):
    for i in words.keys():
        if i == checkWord:
            return True

def add_Word(status, addWord):
    if status != True:
        definition = input("Enter new definition of the word\n >> ").lower()
        if definition == "":
            print("Definition of the word cannot be empty!")
            pass
        else:
            words[addWord] = definition
            print("Word added!")
            print(words)
    else:
        print(f"{addWord} already exists!")
    
    # else:
    #     print("Please enter a word!")

def Admin_panel():
    while isFound:
        try:
            selection = menu()
            selection = int(selection)
            while selection != 5:
                if selection == 1:
                    status = False
                    checkWord = input("Please enter a word\n >> ").lower()
                    status = check_word(checkWord)
                    add_Word(status, checkWord)
                    selection = menu()
                    selection = int(selection)
                # match selection:
                #     case "1":
                #         status, checkWord = mainframe.check_word()
                #         mainframe.add_Word(status, checkWord)
                #         pass
                #     case 2:
                #         mainframe.Del_word(status)
                #         pass
                #     case 3:
                #         pass
                #     case 4:
                #         print("Men")
                #     case 5:
                #         print("Exit")
                #     case _:
                #         print("Please type in a selection within 1 to 4!")
        except:
            print("Pls enter a number")
