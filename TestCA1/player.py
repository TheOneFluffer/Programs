import random
import generalMethods as gm

def playMenu():  
    """ This method prints the play menu """
    print("Please select a difficulty level")
    print("[1] Easy")
    print("[2] Standard")
    print("[0] Back to main menu")
    print("Enter your choice")
    diff_choice = gm.validateChoice(">> ", 0, 2)
    return diff_choice

def readWordList(filename, wordlist):
    """ This method reads from filename variable & creates a dictionary """
    file = open(filename, "r")

    # Get key-value pair for dictionary
    for line in file:
        key = line.split(':')[0]
        value = line.split(':')[1].replace('\n', '')
        wordlist[key] = value

    file.close()
    return wordlist

def getRandomWords(wordlist, wordsplayed, times):
    """ This method selects a random word & meaning to be returned """
    words = ""
    counter = 1

    while len(wordsplayed) < times:
        word, meaning = random.choice(list(wordlist.items()))
        wordsplayed.append(word)

        if word == wordsplayed[counter-1] and len(wordsplayed) > 1:
            wordsplayed.pop(counter)
        elif word != wordsplayed[counter-1] and len(wordsplayed) > 1:
            counter += 1

    words += f"The {times} words are: "
    for i in wordsplayed:              
        words += i + " "

    gm.logOutToLogs(f"The chosen words are: {words}")
    gm.logOutToReport(f"The chosen words are: {words}")

    return word, wordsplayed

def startGame(gamesPlayed, word, wordlist, diff_choice, tries, points):
    """ This method loops & prints the game """
    deductBy = 1
    check = 0
    guessed = False
    startOfGame = True
    incorrect_chars = []
    correct_chars = []
    char = ""

    while not guessed and tries > 0:
        # print game round
        if startOfGame:
            print(f"G A M E {gamesPlayed}")
            startOfGame = False
        else:
            # set difficulty level
            if diff_choice == 2:
                deductBy = 2
            
            # first print
            if tries == 10 and len(correct_chars) == 0:
                print(determineHangMan(tries))

                for i in word:
                    print("_", end="")

                print("\n")
            elif tries > 0 and len(correct_chars) > 0:
                printCorrectAns(word, correct_chars)
            elif tries > 0 and len(incorrect_chars) > 0:
                for i in word:
                    print("_", end="")
                
            char = checkLetterExists("\nSelect a valid character [a-z]: ", char, correct_chars, incorrect_chars)

            tries, correct_chars, check, points = gameLogic(char, word, tries, deductBy, incorrect_chars, correct_chars, check, points)
            guessed, tries = checkIfWon(tries, word, wordlist, guessed, check)
          
    return guessed, tries, gamesPlayed, points

def checkLetterExists(prompt, char, correct_chars, incorrect_chars):
    """ This method validates if the letters already exists """
    while True:
        try:  
            char = input(prompt).lower()
            if len(char) == 1:
                if char in correct_chars or char in incorrect_chars:                   
                    print(f"Sorry, please re-enter a character that is unused") 
                elif not char.isalpha():
                    print(f"Sorry, please re-enter a valid character from [a-z]") 
                else:
                    return char 
            else:
                print(f"Sorry, please only enter 1 character from  [a-z]") 
        except:
            print(f"Sorry, please re-enter a valid character from [a-z]")  

def gameLogic(char, word, tries, deductBy, incorrect_chars, correct_chars, check, points):
    """ This method determines if the character entered is correct/incorrect and displays the hangman art """
    got_letter = False

    for i in word:
        if i == char:
            got_letter = True
            check += 1
            points += 2

    if got_letter == False:
        tries -= deductBy
        print(determineHangMan(tries))
        incorrect_chars.append(char)
        print("\nIncorrect characters:", end=" ")

        for i in incorrect_chars:
            print(i, end=" ")
    else:
        print(determineHangMan(tries))
        correct_chars.append(char)
        
    print("\n\n")
            
    return tries, correct_chars, check, points

def checkIfWon(tries, word, wordlist, guessed, check):
    """ This method determines if the user won or lost """
    meaning = wordlist[word.title()]

    if tries > 0 and check == len(word):
        guessed = True
        print(f"Congratulations. The word is {word}: {meaning}\n")
    elif tries == 0 and check < len(word):
        print(f"Maximum number of guesses!\nThe word is {word}: {meaning}\n")

    return guessed, tries

def printCorrectAns(word, correct_chars):
    """ This method prints the word and its blanks """
    for i in range(len(word)):
        if word[i] in correct_chars:
            print(word[i], end="") 
        else:
            print("_", end="")
        
def determineHangMan(tries):
    """ This method contains all the hangman art and can be returned with number of tries """
    stages = [  """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |   / \\
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |   / 
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|\\
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
         |   [O]
         |   /|\\
         |   
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|
         |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |    | 
         |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |    
         |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O
         |     
         |
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
         |     
         |
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
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    
         |    
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

def checkHighScore(name, highscore, points, namedict, highscore_file):
    """ This method checks if user won/lost the game and if they have a highscore """
    gm.logOutToLogs(f"{name} scored {points} points")
    gm.logOutToReport(f"{name} scored {points} points")
    if points <= 15:
        print("Sorry, you have lost the game.")
    elif points > highscore:
        updateHighscore(name, points, namedict, highscore_file)
    else:
        print("You have won the game.")

def updateHighscore(name, highscore, namedict, highscore_file):
    """ This method updates the score of the user in userlist.txt if they have a new highscore """
    new  = 0

    for i in namedict.keys():
        if i == name:
            namedict[i] = highscore
        else:
            new += 1

    if new == len(namedict):
        namedict[name] = highscore

    with open(highscore_file, 'w') as file:
        for i, j in namedict.items():       
            file.write(f"{i},{j}\n")

    print("You have won the game with a new highscore!")
    gm.logOutToReport(f"{name} won the game with a new highscore of: {highscore}")

def playGame(name, highscore, namedict, highscore_file, gamesPlayed, wordlist, diff_choice):
    """ This method checks if 3 rounds are being played by the user """
    tries = 10
    points = 0
    wordsplayed = []
    word = ""
    meaning = ""
    game_ctr = 0
    times = 3

    print("\nH A N G M A N")
    print(f"Player: {name}")

    word, wordsplayed = getRandomWords(wordlist, wordsplayed, times)

    while gamesPlayed <= times:
        if game_ctr < times:
            word = wordsplayed[game_ctr].lower()
            # print(word)
            guessed, tries, gamesPlayed, points = startGame(gamesPlayed, word, wordlist, diff_choice, tries, points)

            # if guessed then increment
            if guessed and tries > 0 or not guessed and tries == 0:
                gamesPlayed += 1
                game_ctr += 1
                tries = 10

            # if gamesPlayed == 3, automatically quit this
            if gamesPlayed > 3:
                print(f"End of game!")
                print("-------------------------------------------------------------------------")

                # cap points
                if points > 30:
                    points = 30

                # check high score
                checkHighScore(name, highscore, points, namedict, highscore_file)                           

                # go back main menu
                diff_choice = 0    

    return gamesPlayed, diff_choice

def play(name, highscore, namedict, highscore_file, settings):
    """ This method is called to run from main. Difficulty level is also determined here. """
    diff_choice = 4
    wordlist = {}
    gamesPlayed = 1
    simple_filename = r"I:\Year 1 Sem 2\PSEC\Programs\TestCA1\simple_wordlist.txt"
    hard_filename = r"I:\Year 1 Sem 2\PSEC\Programs\TestCA1\hard_wordlist.txt"

    while (diff_choice != 0 and gamesPlayed < 3):
        diff_choice = playMenu()
        if (diff_choice == 1):
            wordlist = readWordList(simple_filename, wordlist)
            gamesPlayed, diff_choice = playGame(name, highscore, namedict, highscore_file, gamesPlayed, wordlist, diff_choice)
        elif(diff_choice == 2):
            wordlist = readWordList(hard_filename, wordlist)
            gamesPlayed, diff_choice = playGame(name, highscore, namedict, highscore_file, gamesPlayed, wordlist, diff_choice)
        else:
            break   
     
def topPlayers(namedict, settings):
    """ This method prints out top players of the game """
    counter = 0

    print("\nH I G H S C O R E")
    sorted_namedict = sorted(namedict.items(), key=lambda x: x[1], reverse=True)
    for i in sorted_namedict:    
        if counter < settings["numberoftopplayers"]:
            counter += 1
            print(f"{counter}: {i[0]} - {i[1]}")

def Credits():
    print("\n")
    print(".-=~=-.                                                                 .-=~=-.")
    print("(__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)")
    print("( _ __) Property of FlufCorp  Property of FlufCorp  Property of FlufCorp( _ __)")
    print("(__  _)                                                                 (__  _)")
    print("(_ ___)                 ♥Welcome to the credits page 1♥                 (_ ___)")
    print("(__  _)                    This segment is made by                      (__  _)")
    print("( _ __)                   Hong Wei from DISM/FT/1B/08                   ( _ __)")
    print("(__  _)                   CEO of FlufCorp Pte Ltd 2022                  (__  _)")
    print("(_ ___)   I will like to take my time to thank the reader for finding   (_ ___)")
    print("(__  _)            and a big shoutout to Mr Lim for all the             (__  _)")
    print("( _ __)    help that I received during these lessons during the past    ( _ __)")
    print("(__  _)                    few lessons. Therefore...                    (__  _)")
    print("(_ ___)                                                                 (_ ___)")
    print("(__  _)                                                                 (__  _)")
    print("( _ __)                                                                 ( _ __)")
    print("(__  _)                                                                 (__  _)")
    print("(_ ___)                     Thank you for reading!!                     (_ ___)")
    print("(__  _)         From the up and coming ethical hacker/programmer        (__  _)")
    print("( _ __)                                                                 ( _ __)")
    print("(__  _)                                                                 (__  _)")
    print("( _ __)                                                                 ( _ __)")
    print("(__  _) Property of FlufCorp  Property of FlufCorp  Property of FlufCorp(__  _)")
    print("(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)")
    print("`-._.-'                                                                 `-._.-'")
    print("\n")
    pass
    Cont = input("Enter [Y]es to see page 2 or [N] to stop: ").upper()
    
    if Cont == "Y":
        print("\n")
        print(".-=~=-.                                                                 .-=~=-.")
        print("(__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)")
        print("( _ __) Property of FlufCorp  Property of FlufCorp  Property of FlufCorp( _ __)")
        print("(__  _)                                                                 (__  _)")
        print("(_ ___)                ♥Welcome to the credits page 2♥                  (_ ___)")
        print("(__  _)                             Socials                             (__  _)")
        print("( _ __)            Github: https://github.com/TheOneFluffer             ( _ __)")
        print("(__  _)                                                                 (__  _)")
        print("(_ ___)  Linkedin: https://www.linkedin.com/in/lau-hong-wei-966b43247/  (_ ___)")
        print("(__  _)                                                                 (__  _)")
        print("( _ __)       Instagram: https://www.instagram.com/sir_fluffbuns/       ( _ __)")
        print("(__  _)                                                                 (__  _)")
        print("(_ ___)                    Were you expecting more?                     (_ ___)")
        print("(__  _)                                                                 (__  _)")
        print("( _ __)                                                                 ( _ __)")
        print("(__  _)                                                                 (__  _)")
        print("(_ ___)                        That's all folks!!                       (_ ___)")
        print("(__  _)         From the up and coming ethical hacker/programmer        (__  _)")
        print("( _ __)                                                                 ( _ __)")
        print("(__  _)                                                                 (__  _)")
        print("( _ __)                                                                 ( _ __)")
        print("(__  _) Property of FlufCorp  Property of FlufCorp  Property of FlufCorp(__  _)")
        print("(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)")
        print("`-._.-'                                                                 `-._.-'")
        print("\n")
        return

    elif Cont == "N":
        return

    else:
        print("Please type in Y to continue or N to stop")
        pass