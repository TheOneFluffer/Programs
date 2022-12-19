import datetime

def validateChoice(prompt, min, max):
    """ This method validates menu choices """
    while True:
        try:
            value = int(input(prompt))
        
            if min <= value <= max:
                return value
                    
            print(f"Sorry, please re-enter a valid choice from ({min}-{max})")   
        except:
            print(f"Sorry, please re-enter a valid choice from ({min}-{max})")  

def logOutToLogs(logline):
    log_file = r"I:\Year 1 Sem 2\PSEC\Programs\TestCA1\gamelog.txt"
    date_time = datetime.datetime.now()
    file = open(log_file, "a")  
    file.write(date_time.strftime("%c: ") + logline + "\n")
    file.close()

def logOutToReport(logline):
    log_file = r"I:\Year 1 Sem 2\PSEC\Programs\TestCA1\report.txt"
    date_time = datetime.datetime.now()
    file = open(log_file, "a")  
    file.write(date_time.strftime("%x: ") + logline + "\n")
    file.close()
