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
number =  int(input("Please enter a number or Q to stop: "))
number_total = number

while number == "Q":
    number_total = number_total + number
    print(f"Current total is {number_total}")
    number = number.upper()
    # if (number == "Q"):
    #     break
