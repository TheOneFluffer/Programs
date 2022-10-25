no1 = int(input("number1: "))
no2 = int(input("number2: "))
no3 = no1 * no2
#print(type(no3))

if (no3 <= 1000):
    print("The result is " , no3)
else:
    no3 = no1 + no2
    print("The result is " , no3)