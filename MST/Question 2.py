a = int(input("Enter first side of triangle: "))
b = int(input("Enter second side of triangle: "))
c = int(input("Enter third side of triangle: "))

if (a + b > c) and (b + c > a) and (c + a > b):
    print("Triangle is possible")
    if (a == b == c):
        print("Equilateral Triangle")
    elif (a != b != c):
        print("Scalene Triangle")
    elif (a == b) or (b == c) or (c == a):
        print("Isosceles Triangle")
else:
    print("Triangle not possible")