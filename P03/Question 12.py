open_ports = {}

enterService = input("Please enter service: port that were found to be open, separated by '|': ")
enterService = enterService.split(sep="|")
open_ports.update({enterService})
print(open_ports)
print("These are the open ports found and their corresponding services:", open_ports[25], open_ports[80], open_ports[443], open_ports[21], open_ports[22], open_ports[23])
print("1. Search for open port\n2. Search for service running\n3. Update dictionary")


# while True:
#     choice = menu()
#     if choice == 1:
