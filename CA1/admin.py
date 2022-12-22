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
    Add, delete or edit words in dictionary
    Report

Credit:
    https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c Hangman ASCII github
    https://www.youtube.com/watch?v=m4nEnsavl6w Hangman Tutorial
    https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary How to convert a file into a dictionary?
    https://pynative.com/python-delete-lines-from-file/ Delete Lines From a File in Python
    https://stackoverflow.com/questions/33631615/how-to-search-range-with-intervals-in-python Searching for details with range
    https://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates Print all day-dates between two dates
"""

import generalMethods as gm
from datetime import *
import os


def adminMenu():  
    """ This method prints the admin menu """
    print("\nA D M I N M E N U")
    print("Please select the task")
    print("[1] Add a new word to a new list")
    print("[2] Add a new word to an existing list")
    print("[3] Edit a word in an existing list")
    print("[4] Delete a word from an existing list")
    print("[5] Read Report")
    print("[6] Edit settings")
    print("[0] Back to main menu")
    print("Enter your choice")
    a_choice = gm.validateChoice(">> ", 0, 6)
    return a_choice

def ifwordExists(word, list):
    '''This function checks if word exists'''
    exists = False
    for key in list.keys():  
        if word == key:
            exists = True
    return exists

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def newWord_in_newList(): #for Option 1
    '''This function appends new word in new wordlist'''
    new_wordlist = input('Please enter a new wordlist name: ').replace(" ", "")
    filepath = r"I:\Year 1 Sem 2\PSEC\Programs\CA1\\" + new_wordlist + ".txt"
    if os.path.exists(filepath) == False and new_wordlist != "":
        print("New wordlist created!")
        new_word = input("Please enter a new word: ").title()
        if new_word != "":
            new_definition = input("Please enter definition for the new word: ")
            if new_definition != "":
                f = open(filepath, "a")
                f.write(new_word + ":" + new_definition + "\n")
                f.close()
                print("Operation completed")
                gm.logOutToReport(f"Admin added new word: {new_word} and the definition is {new_definition} to a new list: {new_wordlist}.txt")
            else:
                print("Definition cannot be empty")
        else:
            print("New word cannot be empty")
    elif new_wordlist == "":
        print("New wordlist cannot be empty!")
    else:
        print("Wordlist already exists!")

def newWord_in_existingList(): #for Option 2
    '''This function appends new word in existing wordlist'''
    word_list = {}
    exists = False

    wordlist = input('Please enter a existing wordlist name: ').replace(" ", "")
    filepath = r"I:\Year 1 Sem 2\PSEC\Programs\CA1\\" + wordlist + ".txt" 
    if os.path.exists(filepath) == True: 
        with open(filepath) as f: 
            word_list = dict(i.rstrip().split(":", 1) for i in f) 
            new_word = input("Please enter a new word: ").title()
            if new_word != "":
                exists = ifwordExists(new_word, word_list)
            else:
                print("New word cannot be empty!")
                return

            if exists == False:
                new_definition = input("Please enter definition for the new word: ")
                if new_definition != "":
                    f = open(filepath, "a")
                    f.write(new_word + ":" + new_definition + "\n")  
                    f.close()  
                    print("Operation completed")
                    gm.logOutToReport(f"Admin has added a new word to {wordlist}.txt. The word is {new_word} and the definition is {new_definition}")
                else:
                    print("Definition cannot be empty")
            else:
                print("Word already exists")  
    else: 
        print("Wordlist doesn't exist!") 

def edit_word_in_existingList(): #for Option 3
    '''This function edits existing word definition in existing wordlist'''
    word_list = {} 
    exists = False

    wordlist = input('Please enter a existing wordlist name: ').replace(" ", "") 
    filepath = r'I:\Year 1 Sem 2\PSEC\Programs\CA1\\' + wordlist + '.txt' 
    if os.path.exists(filepath) == True: 
        with open(filepath) as f:
            '''Dump txt file into dictionary '''
            word_list = dict(i.rstrip().split(":", 1) for i in f)
            existing_word = input("Please enter a existing word: ").title()
            if existing_word == "":
                print("Existing word cannot be empty!")
                return
            else:
                exists = ifwordExists(existing_word, word_list)

            if exists == True:
                '''Logic is to update definition of the word'''
                new_definition = input("Please enter definition for the existing word: ")
                if new_definition != "":
                    word_list[existing_word] = new_definition
                    with open(filepath, "w") as f:
                        for key, value in word_list.items():
                            f.write('%s:%s\n' % (key, value))
                    print("Operation completed")
                    gm.logOutToReport(f"Admin has edited the definition to {existing_word}: {new_definition} from {wordlist}.txt")
                else:
                    print("New definition cannot be empty")
                
            else:
                print("Word is not found!")
    else: 
        print("Wordlist doesn't exist!")

def delete_word_in_existingList(): #for Option 4
    '''This function delete existing word in existing wordlist'''
    word_list = {} 
    exists = False

    wordlist = input('Please enter a existing wordlist name: ').replace(" ", "") 
    filepath = r'I:\Year 1 Sem 2\PSEC\Programs\CA1\\' + wordlist + '.txt' 
    if os.path.exists(filepath) == True: 
        with open(filepath) as f:
            '''Dump txt file into dictionary '''
            word_list = dict(i.rstrip().split(":", 1) for i in f)
            existing_word = input("Please enter a existing word to delete: ").title()
            if existing_word == "":
                print("Existing word cannot be empty!")
                return
            else:
                exists = ifwordExists(existing_word, word_list)

            if exists == True:
                '''Logic is to delete both word and definition in the txt file'''
                del word_list[existing_word]
                with open(filepath, "w") as f:
                    for key, value in word_list.items():
                        f.write('%s:%s\n' % (key, value))
                print("Operation completed")
                gm.logOutToReport(f"Admin has deleted the word {existing_word} from {wordlist}.txt")
                
            else:
                print("Word is not found!")
    else:
        print("Wordlist doesn't exist!")

def readReport():
    print("\nReport reading")
    print("[1] Print full report")
    print("[2] Custom report")
    print("[0] Exit")
    print("Enter your choice")
    choice = gm.validateChoice(">> ", 0, 2)

    if choice != 0:
        if choice == 1:
            '''This method reads and display reports'''
            gameReport = r"I:\Year 1 Sem 2\PSEC\Programs\CA1\\report.txt"
            f = open(gameReport, "r")
            for show in f:
                print(show)
        
        elif choice == 2:
            '''The part is to print'''
            gameReport = open("I:\Year 1 Sem 2\PSEC\Programs\CA1\\report.txt", "r")
            data = gameReport.read()
            report2List = data.split('\n')
            gameReport.close()
            print(f"\nStart: {report2List[0]} End: {report2List[-2]}\n")

            day1, month1, year1 = [int(x) for x in input("Please specify start date(format dd/mm/yyyy): ").split('/')]
            date1 = date(year1, month1, day1)
            day2, month2, year2 = [int(x) for x in input("Please specify end date(format dd/mm/yyyy): ").split('/')]
            date2 = date(year2, month2, day2)

            if date1 == "" and date2 == "":
                print("Start or End is invalid!")
                return
            else:
                '''Slice report file for needed info'''
                if date1 > date2:
                    print("End date cannot be bigger than Start date!")
                    return
                elif date1 < date2:
                    logs = ""
                    readReport = open("I:\Year 1 Sem 2\PSEC\Programs\CA1\\report.txt", "r")
                    for i in readReport:

                        logDate = datetime.strptime(str(i[0:10]), '%d/%m/%Y').date()
                        if logDate >= date1 and logDate <= date2:
                            logs += i
                    print(logs)
    else:
        return

def editSetting():
    '''This function allows admin to edit settings.txt'''
    word_list = {}
    gameSettings = "I:\Year 1 Sem 2\PSEC\Programs\CA1\gamesettings.txt"
    print("~Settings Page~")
    print("[1] Edit number of attempts")
    print("[2] Edit the number of words")
    print("[3] Edit the number of top players")
    print("[0] Exit")
    print("Enter your choice")
    choice = gm.validateChoice(">> ", 0, 3)
    
    if choice != 0:
        if choice == 1:
            '''This method allows users to edit number of attempts'''
            with open(gameSettings) as f:
                word_list = dict(i.rstrip().split(":", 1) for i in f)
                editAttempt = input("Number of attempts (default: 3): ") or 3
                if editAttempt != "":
                    word_list["numberofattempts"] = int(editAttempt)
                    with open(gameSettings, "w") as f:
                        for key, value in word_list.items():
                            f.write('%s:%s\n' % (key, value))
                else:
                    word_list["numberofattempts"] = editAttempt
                    print("Number of attempts are unchanged")
        
        elif choice == 2:
            '''This method allows users to edit number of words'''
            with open(gameSettings) as f:
                word_list = dict(i.rstrip().split(":", 1) for i in f)
                editWords = input("Number of words per session (default: 3): ") or 3
                if editWords != "":
                    word_list["numberofwords"] = int(editWords)
                    with open(gameSettings, "w") as f:
                        for key, value in word_list.items():
                            f.write('%s:%s\n' % (key, value))
                else:
                    word_list["numberofwords"] = editWords
                    print("Number of words are unchanged")

        elif choice == 3:
            '''This method allows users to edit number of top players'''
            with open(gameSettings) as f:
                word_list = dict(i.rstrip().split(":", 1) for i in f)
                editPlayers = input("Number of players to display (default: 5): ") or 5
                if editPlayers != "":
                    word_list["numberoftopplayers"] = int(editPlayers)
                    with open(gameSettings, "w") as f:
                        for key, value in word_list.items():
                            f.write('%s:%s\n' % (key, value))
                else:
                    word_list["numberofwords"] = editPlayers
                    print("Number of top players are unchanged")
    else:
        return

def adminPanel(name):
    a_choice = 6
    
    while a_choice != 0:
        if a_choice != 0:
            a_choice = adminMenu()
        
            if a_choice == 1:
                '''Add a new word to a new list'''
                newWord_in_newList()
            elif a_choice == 2:
                '''Add a new word to an existing list'''
                newWord_in_existingList()
            elif a_choice == 3:
                '''Edit a word in an existing list'''
                edit_word_in_existingList()
            elif a_choice == 4:
                '''Delete a word from an existing list'''
                delete_word_in_existingList()
            elif a_choice == 5:
                '''Read game logs that are saved as gamelog.txt'''
                readReport()
            elif a_choice == 6:
                '''Edit game settings'''
                editSetting()
        elif a_choice == 0:
                gm.logOutToReport("Admin has logged out!")
                pass
        else:
            name = "Admin"
            return name