# for number in range(8, 2, -1):
#     print(number, end=" ")

#Question 1
# number = input("Enter a number: ")

# if (number.isnumeric() == False):
#     print("You did not enter a number")
# elif (int(number) % 2 != 0):
#     print(f"{number} is odd")
# else:
#     print(f"{number} is even")

#Question 2
# number1 = input("Enter a number: ")
# number2 = input("Enter another number: ")

# if (number1.isnumeric() == False):
#     print("You didn't enter a number")
# elif (number2.isnumeric() == False):
#     print("You didn't enter a number")
# elif (int(number1) > int(number2)):
#     print(f"{number1} is bigger!")
# elif (int(number1) < int(number2)):
#     print(f"{number2} is bigger!")
# else:
#     print("Both numbers are the same!")

# #Question 3
# years = input("Enter number of years in service: ")
# salary = input("Enter current salary: ")

# if (years.isnumeric() == False):
#     print("It is not a number")
# elif (salary.isnumeric() == False):
#     print("It is not a number")
# else:
#     if (int(years) < 10):
#         if (int(salary) < 1000):
#             print("Your increment is $100")
#         elif (int(salary) < 2000):
#             print("Your increment is $200")
#         else:
#             print("Your increment is $300")
#     if (int(years) > 10):
#         if (int(salary) < 1000):
#             print("Your increment is $200")
#         elif (int(salary) < 2000):
#             print("Your increment is $300")
#         else:
#             print("Your increment is $400")

#Question 4
# number1 = int(input("Enter a starting number: "))
# number2 = int(input("Enter a ending number: "))

# if (number1 > number2):
#     for i in range(number1, number2, -1):
#         if (i % 2 == 1):
#             print(i, end="\t")
#         else:
#             pass
# else:
#     for i in range(number1, number2, 1):
#         if (i % 2 == 1):
#             print(i, end="\t")
#         else:
#             pass

#Question 5
# number1 = int(input("Enter a starting number: "))
# number2 = int(input("Enter a ending number: "))

# if (number1 > number2):
#     for i in range(number1, number2, -1):
#         if (i % 2 == 0):
#             print(i, end="\t")
#         else:
#             pass
# else:
#     for i in range(number1, number2, 1):
#         if (i % 2 == 0):
#             print(i, end="\t")
#         else:
#             pass

#Question 6
# number = ""
# number_total = 0

# while number != "Q":
#     number = input("Please enter a number or Q to stop: ")
#     if (number.isnumeric() == False and number == "Q"):
#         print(f"Final sum is {number_total}")
#         break
#     elif (number.isnumeric() == False and number != "Q"):
#         print("Please enter a valid number!")
#     else:
#         number_total = int(number) + number_total
#         print(f"Current total is {number_total}")

#Question 7
# number = ""
# while True:
#     try:
#         number = int(input("Enter a number: "))
#         print("Great, you have successfully entered an integer")
#     except ValueError as ve:
#         print("No valid integer! Please try again ...")

#Question 8
# number = ""

# while True:
#     try:
#         number = int(input("Enter a number: "))
#         if int(number) % 2 == 0:
#             print(f"{number} is even")
#             break
#         else:
#             print(f"{number} is odd")
#             break
#     except TypeError as ve:
#         print("You did not enter a number")
#     except ValueError as ve:
#         print("You did not enter a number")
selection = 0
number = 0
number2 = 0
number_total = 0

def evenodd():
    number = int(input("Enter a number: "))
    if (number % 2 == 0):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

def bigsmall():
    number = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    if (number > number2):
        print(f"{number} is bigger!")
    else:
        print(f"{number2} is bigger!")

def Q2stop():
    while number != "Q":
        number = input("Please enter a number or Q to stop: ")
        if (number.isnumeric() == False and number == "Q"):
            print(f"Final sum is {number_total}")
        elif (number.isnumeric() == False and number != "Q"):
            print("Please enter a valid number!")
        else:
            number_total = int(number) + number_total
            print(f"Current total is {number_total}")

def printrange():
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

while True:
    print("\n1. Determine odd or even \n2. Determine bigger number \n3. Find sum of numbers \n4. Display even numbers, inclusive")
    selection = int(input("Enter a choice: "))
    
    match selection():
        case 1:
            evenodd()
