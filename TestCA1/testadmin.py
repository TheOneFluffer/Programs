from datetime import datetime
from datetime import *
import generalMethods as gm

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def readReport():
    print("\nReport reading")
    print("[1] Print full report")
    print("[2] Custom report")
    print("[0] Exit")
    print("Enter your choice")
    choice = gm.validateChoice(">> ", 0, 2)

    if choice != 0:
        if choice == 1:
            '''This method reads and display reports'''
            gameReport = r"I:\Year 1 Sem 2\PSEC\Programs\TestCA1\\report.txt"
            f = open(gameReport, "r")
            for show in f:
                print(show)
        
        elif choice == 2:
            '''The part is to print'''
            gameReport = open("I:\Year 1 Sem 2\PSEC\Programs\TestCA1\\report.txt", "r")
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
                    readReport = open("I:\Year 1 Sem 2\PSEC\Programs\TestCA1\\report.txt", "r")
                    for i in readReport:

                        logDate = datetime.strptime(str(i[0:10]), '%d/%m/%Y').date()
                        if logDate >= date1 and logDate <= date2:
                            logs += i
                    print(logs)
    else:
        return

readReport()