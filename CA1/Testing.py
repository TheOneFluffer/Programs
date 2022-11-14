# import random
# # import json
# from word_list import words
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

file1 = open("Hi-score.txt","r")
file1.close()







vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
    }
def rand_func(word):
    for i in word: #get vowels
        if i in vowels:
            vowels[i] += 1
    return vowels

word = input("Please enter a word: ")
print(rand_func(word))