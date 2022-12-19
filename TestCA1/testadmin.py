def readReport():
    '''This method reads and display game report and it allows you to specify start and end dates'''
    gameReport = r"I:\Year 1 Sem 2\PSEC\Programs\TestCA1\report.txt"
    f = open(gameReport, "r")

    for show in f:
        print(show)

    with open(gameReport) as f: 
        Report = dict(i.rstrip().split(":", 1) for i in f)
        searchStart = input("Please enter a start time (format mm/dd/yy): ").replace(" ", "/")
        searchEnd = input("Please enter a end time (format mm/dd/yy): ").replace(" ", "/")
        if searchStart == "" and searchEnd == "":
            print("Start or End cannot be empty!")
            return
        else:
            '''Take start and end and look up'''
            for i in f:
                print(i)
 
readReport()