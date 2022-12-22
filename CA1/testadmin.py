import generalMethods as gm

def editSetting():
    '''This function allows admin to edit settings.txt'''
    word_list = {}
    gameSettings = "I:\Year 1 Sem 2\PSEC\Programs\TestCA1\gamesettings.txt"
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

editSetting()