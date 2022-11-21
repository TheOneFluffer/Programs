# import random
import json
from new_wordlist import words
# # portlist = {25:"SMTP",80:"HTTP",443:"HTTPS",23:"TELNET"}

# # portlist.items()
# # for port, service in portlist.items():
# #   print(f"{port}: {service}")
# category_key = list((words.keys())) #simple is a dictionary
# word = (random.randint(0, len(category_key) - 1)) #generate random word
# rand_word = category_key[word]
# rand_def = words[rand_word]
# print(f'{rand_word}: {rand_def}')



# Enter a number: 5

# 1   2   3   4   5
# 2   4   6   8   10
# 3   6   9   12  15
# 4   8   12  16  20
# 5   10  15  20  25

# Enter a number: 3

# 1   2   3   
# 2   4   6   
# 3   6   9   

# username = "Ivan"
# points_earned = 5
# def point_system(username, points):

# file1 = open("Hi-score.txt","r")
# file1.close()







# vowels = {
#     "a": 0,
#     "e": 0,
#     "i": 0,
#     "o": 0,
#     "u": 0
#     }
# def rand_func(word):
#     for i in word: #get vowels
#         if i in vowels:
#             vowels[i] += 1
#     return vowels

# word = input("Please enter a word: ")
# print(rand_func(word))
# def Difficulty_selection():
#     difficulty_settings = input
#     if difficulty_settings == 1:
#         tries = 10
#     elif difficulty_settings == 2:
#         tries = 5
#     elif difficulty_settings == 3:
#         tries = 3
#     return tries

# isFound = True

# while isFound:
#     try:
#         print("Please select difficulty level:\n 1. Easy\n 2. Normal\n 3. Hard") #Allows selection of difficulty)
#         selection = input('> ')
#         selection = int(selection)
#         if selection != 5:
#             match selection:
#                 case 1:
#                     tries = 10
#                 case 2:
#                     tries = 5
#                     pass
#                 case 3:
#                     tries = 3
#                     # print("Star walkinnn")
#                 case _:
#                     print("Please type in a selection within 1 to 4!")
#         else:
#             break
#     except:
#         print("Pls enter a number")

# print("Hi-scores of other players: ")
# f = open('Highscore.txt')
# list(f)
# with open('Highscore.txt', 'r') as reader:
#     #Read and print the entire file line by line
#     line = reader.readline()
#     while line != '':
#         print(line, end='')
#         line = reader.readline()

checkWord = input("Please enter a word\n >> ").lower()
def check_word(checkWord):
    for i in words.keys():
        if i == checkWord:
            return True
        else:
            return False

status = check_word(checkWord)

def add_Word(status, addWord):
    if status == False:
        definition = input("Enter new definition of the word\n >> ").lower()
        if definition == "":
            print("Definition of the word cannot be empty!")
            pass
        else:
            words[addWord] = definition
            print("Word added!")
            print(words)

    elif status == True:
        print(f"{addWord} already exists!")
    
    else:
        print("Please enter a word!")

def del_Word(status, delword):
    if status == True:
        YorN = input(f"Are you sure you want to delete {delword}? [Y]es / [N]o\n >> ").upper()
        if YorN == "Y":
            del words[delword]
            print("Word deleted")
            print(words)

        elif YorN == "N":
            pass
        
        else:
            print("Please type [Y]es or [N]o\n >> ")
            pass
        
    else:
        if delword == "":
            print("Word to delete cannot be empty")
            pass
        else:
            print("The word you are looking for doesn't exist!")
            pass

add_Word(status, checkWord)
# del_Word(status, checkWord)
