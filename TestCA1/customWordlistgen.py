def wordExist():
    new_wordlist = input('Please enter a new wordlist name: ')
    filename = r"I:\\Year 1 Sem 2\\PSEC\\Programs\\TestCA1\\" + new_wordlist + ".txt"
    try:
        f = open(filename, "r")
        for l in f:
            print(l)
    except:
        return "new"

wordExist()
