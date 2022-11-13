'''
Credits: 
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c Hangman ASCII github
https://www.youtube.com/watch?v=m4nEnsavl6w Hangman Tutorial
'''

import random
from Color import category

def get_word():
    print(f"\nSelect the category from the following list: {list(category.keys())}")
    category_key = input("\nEnter the category name: ").lower()
    word = random.choice(category[category_key])
    return word.lower()

def play(word, username):
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
        print(f"Congratulations, The secret word is {word}. You win")
    else:
        print("Maximum number of guesses!")
        print(f"After 5 incorrect guesses, The word was", word)
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

def username():
    username = input("Please enter name: ")
    return username

def main():
    word = get_word()
    username = input("Please enter name: ")
    play(word, username)
    while input("Enter [Y]es to play again or [N] to quit: ").lower() == "y":
        word = get_word()
        play(word, username)

if __name__ == "__main__":
    main()
