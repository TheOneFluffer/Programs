#Question 4
number1 = input("Enter a starting number: ")
number2 = input("Enter a ending number: ")

if (number1.isnumeric() == False):
    print("You didn't enter a number")
elif (number2.isnumeric() == False):
    print("You didn't enter a number")
else:
    if (int(number1) > int(number2)):
        for i in range(number1, number2, 2):
            print(i, space = " ")
            break
    else:
        for i in range(number2, number1, -2):
            print(i, space = " ")