enterFood = input("Please enter your restaurant dishes,separated by comma ',': ")
enterFood = enterFood.split(sep = ", ")
findFood = input("Please input food to search: ")

isFound = True
allFood = 0

for i in enterFood:
    if (findFood.upper() in i.upper()):
        print("Yes, we serve the following: ")
        break

for i in enterFood:
    if (findFood.upper() in i.upper()):
        print(i)
    else:
        isFound = False
        allFood += 1
        #pass

if isFound == False and allFood == len(enterFood):
    print(f"Sorry, we don't serve {findFood}!")
    print(f"Pls choose from {enterFood}")