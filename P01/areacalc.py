# length = input("Enter the length of the square: ")
# length = int(length)
# Area = length * length
# Perimeter = length * 4
# print(f"Area of the square is: {Area}")
# print(f"Perimeter of the square is: {Perimeter}")

#Weight program
weight = int(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = round(weight / (height ** 2), 1)
print(f"Your BMI is {bmi}")