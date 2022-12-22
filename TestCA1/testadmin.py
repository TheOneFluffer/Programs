from datetime import datetime
from datetime import *
import generalMethods as gm

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

editSetting()