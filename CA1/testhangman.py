'''
Credits: 
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c Hangman ASCII github
https://www.youtube.com/watch?v=m4nEnsavl6w Hangman Tutorial
'''

import random
from words import word_list_animals_easy

def get_word():
    word = random.choice(word_list_animals_easy)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("H A N G M A N")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
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
                for index in indexes:
                    word_as_list[index] = guess
                word_completion = "".join(word_completion)
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
        print(word_completion)
        print("\n")
    if guessed:
        print(f"Congratulations, The secret word is {word}. You win")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")

def display_hangman(tries):
    stages = [  """
        _________
        |/      |
        |       O
        |      /|\\
        |       |
        |      / \\
        |
        |_________
        """,
        """
        _________
        |/      |
        |       O
        |      /|\\
        |       |
        |      / 
        |
        |_________
        """,
        """
        _________
        |/      |
        |       O
        |      /|\\
        |       |
        |      
        |
        |_________
        """,
        """
        _________
        |/      |
        |       O
        |      /|
        |       |
        |      
        |
        |_________
        """,
        """
        _________
        |/      |
        |       O
        |       |
        |       |
        |      
        |
        |_________
        """,
        """
        _________
        |/      |
        |       O
        |       
        |       
        |      
        |
        |_________
         """,
        """
        _________
        |/      |
        |       
        |       
        |       
        |      
        |
        |_________
        """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Enter [Y]es to play again or [N] to quit: ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()