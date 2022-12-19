import player as p
import generalMethods as gm
import admin as a

def mainMenu(settings):
    """ This method prints out the main menu """
    print("\nM A I N M E N U")
    print("[1] Play")
    print(f"[2] Select top {settings['numberoftopplayers']} players")
    print("[3] Credits")
    print("[0] Exit")
    print("Enter your choice")
    choice = gm.validateChoice(">> ", 0, 3)
    return choice

def validateUser(filename):
    """ This method validates existence of user """
    name = ""
    print("Please enter your name")
    while name == "":  
        name = input(">> ").title() 
        name = name.replace(" ", "") 
        if name != "":
            exists, namedict = readUserList(filename, name)
            gm.logOutToLogs(name + " has logged in!")
            gm.logOutToReport(name + " has logged in")
            return name, exists, namedict
        else:
            print("Name cannot be empty!")

def readUserList(filename, name):
    """ This method reads from userlist.txt & determines if user exists """
    exists = False
    namedict = {}

    # Open file of filename provided
    file = open(filename, "r")

    # Get key-value pair for dictionary
    for line in file:
        if ',' in line:
            key = line.split(',')[0]
            value = int(line.split(',')[1].replace('\n', ''))
            namedict[key] = value

    file.close()
    
    if name in namedict.keys():
        exists = True

    return exists, namedict 

def playGreeting(name, exists, namedict):
    """ This method displays greeting of new/existing user based on userlist.txt """
    score = 0

    if exists == True:
        for i in namedict.keys():
            if i == name:
                score = namedict[i]

        print(f"\nWelcome back, {name}! Your highscore was: {score}")
        gm.logOutToReport(f"name has logged in, score is {score}")
    else:
        print(f"\nWelcome, {name}!")
        gm.logOutToReport(f"name has logged in")

    return score

def readSettings(settings_file, settings):
    """ This method reads from gamesettings.txt & determines game settings """
    # Open file of filename provided
    file = open(settings_file, "r")

    # Get key-value pair for dictionary
    for line in file:
        if ':' in line:
            key = line.split(':')[0]
            value = int(line.split(':')[1].replace('\n', ''))
            settings[key] = value

    return settings

def main(): 
    choice = ""
    name = ""
    password = ""
    settings = {}
    filename = r"I:\Year 1 Sem 2\PSEC\Programs\TestCA1\userlist.txt"
    settings_file = r"I:\Year 1 Sem 2\PSEC\Programs\TestCA1\gamesettings.txt"

    while (choice != 0):
        # read settings & logs file
        settings = readSettings(settings_file, settings)

        if name != "" and name != None and name != "Admin":
            choice = mainMenu(settings)
        
            if choice != 0:
                if choice == 1:
                    '''Play game'''
                    highscore = playGreeting(name, exists, namedict)
                    p.play(name, highscore, namedict, filename, settings)
                elif choice == 2:
                    '''Show top few players'''
                    p.topPlayers(namedict, settings)
                    pass
                elif choice == 3:
                    p.Credits()
            elif choice == 0:
                break
        elif name == "Admin":
            # show admin panel
            print("Enter password")
            password = input(">> ")
            if (name == "Admin" and password == "qQ1@"):
                name = a.adminPanel(name)
                gm.logOutToLogs("Admin has logged in!")
            else:
                print("Denied login as password is incorrect!\n")
                name, exists, namedict = validateUser(filename)
                gm.logOutToLogs("Denied login as password is incorrect!")
        elif name == None:
            print("Logging off from admin panel...")
            name, exists, namedict = validateUser(filename)
            gm.logOutToLogs("Admin Logged off...")
        else:
            name, exists, namedict = validateUser(filename)

main()