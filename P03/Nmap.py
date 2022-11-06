#Step 1
foundPorts = input("Please enter ports that were found to be open ' | ': ")
foundPorts = foundPorts.split(sep = "|")
userPorts = input("Please input port number for your 'service': ")

isFound = True
allPorts = 0

for i in foundPorts:
    if (userPorts == i):
        print(f"Yes, port {userPorts} is open!")
        break
    else:
        isFound = False
        allPorts += 1

if isFound == False and allPorts == len(foundPorts):
    print(f"Sorry, port {userPorts} is closed! Please choose from {foundPorts}")