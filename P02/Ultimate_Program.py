selection = 0
number = 0
number2 = 0
number_total = 0

while True:
    print("\n1. Determine odd or even \n2. Determine bigger number \n3. Find sum of numbers \n4. Display even numbers, inclusive")
    selection = int(input("Enter a choice: "))
    
    if selection == 1:
        number = int(input("Enter a number: "))
        if (number % 2 == 0):
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    
    elif selection == 2:
        number = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
        if (number > number2):
            print(f"{number} is bigger!")
        else:
            print(f"{number2} is bigger!")
    
    elif selection == 3:
        while number != "Q":
            number = input("Please enter a number or Q to stop: ")
            if (number.isnumeric() == False and number == "Q"):
                print(f"Final sum is {number_total}")
            elif (number.isnumeric() == False and number != "Q"):
                print("Please enter a valid number!")
            else:
                number_total = int(number) + number_total
                print(f"Current total is {number_total}")
    
    elif selection == 4:
        number = int(input("Please enter a starting number: "))
        number2 = int(input("Please enter an ending number: "))
        if (number > number2):
            for i in range(number, number2, -1):
                if (i % 2 == 0):
                    print(i, end="\t")
                else:
                    pass
        for i in range(number, number2, 1):
            if (i % 2 == 0):
                    print(i, end="\t")
            else:
                pass 
    else:
        print("Please select a number!")