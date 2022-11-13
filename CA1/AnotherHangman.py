import random
from Hangman_art import hangman_art
from word_list import wordlist
count = len(hangman_art)
name = input("\nEnter your name: ").title()

print(f"\nSelect the category from the following list:\n{list(wordlist.keys())}")

category_key = input("\nEnter the category name: ").lower() #Select category
chosen_word = random.choice(wordlist[category_key])
word = []
display = ''

for letter in chosen_word:
    word += "_"
    display += letter

print(f"\n Can you guess the word: {word}")

tries = 6

while not tries >= count:
    chosen_letter = input("\nEnter the letter: ").lower()

    if chosen_letter in wordlist:
        wordlist.remove(chosen_letter)
    
        if not chosen_letter in chosen_word:
            print(hangman_art[tries])
            tries -= 1

        for index, letter in enumerate(chosen_word):
            if letter == chosen_letter:
                word[index] = chosen_letter
            print(f"\n{word}")

        if not "_" in word:
            print(f"\nCongrats! {name}, you win the game")
            break

        if tries == count:
            print(f"\nSorry! {name}, you lose the game!")
            break
    else:
        print(f"\n{chosen_letter} is already used, enter another letter.\n")

print(f"\nThe word you had to guess is: {display}\n\nGame Over!\n")