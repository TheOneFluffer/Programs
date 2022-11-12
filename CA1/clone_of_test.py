'''
Credits: 
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c Hangman ASCII github
https://www.youtube.com/watch?v=m4nEnsavl6w Hangman Tutorial
'''

import random
from Animals import word_list_animals_simple
from Animals import word_list_animals_advanced

def get_word():
    word = random.choice(word_list_animals_simple + word_list_animals_advanced)
    return word.lower()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    wrong_letters = []
    guessed_words = []
    tries = 5

    print("H A N G M A N")
    username = input("Please enter name: ")
    print("Player:",username)
    print(display_hangman(tries))
    print("Incorrect letters: ", " ".join(wrong_letters), "(",len(wrong_letters),")" )
    print("\n")
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Select a valid character [a-z]: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter: {guess}")

            elif guess not in word:
                print(f"{guess} is not in the word!")
                tries -= 1
                guessed_letters.append(guess)
                wrong_letters = guessed_letters
                print("Incorrect letters: ", wrong_letters, "(",len(wrong_letters),")" )

            else:
                print(f"Nice, {guess}, is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indexes = [i for i, letter in enumerate(word) if letter == guess]

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
                wrong_letters = guessed_words
                wrong_letters = " ".join(wrong_letters)

            else:
                guess = True
                word_completion = word

        else:
            print("Not a valid guess")

        print("Player:",username)
        print(display_hangman(tries))
        print("Incorrect letters: "," ".join(wrong_letters), "(",len(wrong_letters),")" )
        print("\n")
        print(word_completion)
        print("\n")
        
    if guessed:
        print(f"Congratulations, The secret word is {word}. You win")

    else:
        print("Maximum number of guesses!")
        # print("After", guessed_words" incorrect guesses and "guessed_letters" correct guess(es), the word was "word": Description here")
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")
        print("*****")

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
    word = get_word()
    play(word)
    while input("Enter [Y]es to play again or [N] to quit: ").lower() == "y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()