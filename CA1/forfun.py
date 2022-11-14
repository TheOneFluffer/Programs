'''
Credits: 
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c Hangman ASCII github
https://www.youtube.com/watch?v=m4nEnsavl6w Hangman Tutorial
'''

import random
# import json
from word_list import words

def get_wordndef():
    category_key = list((words.keys())) #simple is a dictionary
    word = (random.randint(0, len(category_key) - 1)) #generate random word
    rand_word = category_key[word]
    rand_def = words[rand_word]
    return rand_word.lower(), rand_def.lower()

def play(word, username, rand_word, rand_def):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 5
    points = 0
    print("H A N G M A N\n")
    print("Player:",username)
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter: {guess}")
            elif guess not in word:
                print(f"{guess}, is not in the word!")
                tries -= 1
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
                tries -= 1
                guessed_words.append(guess)
            else:
                guess = True
                word_completion = word

        else:
            print("Not a valid guess")

        print(display_hangman(tries))
        print("Used letters: "," ".join(guessed_letters), "(",len(guessed_letters),")" )
        print("\n")
        print(word_completion)
        print("\n")
    if guessed:
        print(word, end=": ")# Print the key
        print(f"Congratulations, You win! The secret word is {rand_word}: {rand_def}")
    else:
        print("Maximum number of guesses!")
        print(f"After 5 incorrect guesses, The word was {rand_word}: {rand_def}")
    # return points

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

def main():
    rand_word,rand_def = get_wordndef()
    username = input("Please enter name: ")
    play(rand_word, username, rand_word, rand_def)
    while input("Enter [Y]es to play again or [N] to quit: ").lower() == "y":
        rand_word,rand_def = get_wordndef()
        play(rand_word, username, rand_word, rand_def)

if __name__ == "__main__":
    main()