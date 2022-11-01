#Step 1
foundPorts = input("Please enter ports that were found to be open ' | ': ")
openPorts = foundPorts.split("|")
userPorts = input("Please input port number for your 'service': ")

if userPorts in foundPorts:
    print(f"Yes, port {userPorts} is open!")
else:
    print(f"Sorry, port {userPorts} is closed! Please choose from ['25', '80', '443', '8080']")