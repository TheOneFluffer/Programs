#User selection screen
selection = ""
isFound = True

try:
    selection = input("Welcome to the hangman game: \n 1. Start Game \n 2. Show Hi-Score \n 3. Credits \n 4. Exit \n> ")
    selection = int(selection)
    while selection != 4:
        match selection:
            case 1:
                print("Hi")
                
            case 2:
                print("Hello")
                
            case 3:
                print("Gayshit")

    print("Exitting")
                
except:
    print("Please type in a selection within 1 to 4!")
    pass
