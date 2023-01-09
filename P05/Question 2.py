class Triangle:
    # define constructor with attributes: base and height
    def __init__(triangle, base, height):
        triangle.base = base
        triangle.height = height
        triangle.calculateArea()

    def calculateArea(triangle):
        triangle.area = 0.5 * triangle.base * triangle.height

    def display(triangle):
        print(f"The base of Triangle is: {triangle.base}")
        print(f"The height of Triangle is: {triangle.height}")
        print(f"The area of Triangle is: {triangle.area}")

class TriangularPrism(Triangle):
    # define constructor with attributes: base, height, and length
    def __init__(triangle, base, height, length):
        triangle.base = base
        triangle.height = height
        triangle.length = length

    def volume(triangle):
        #(b * h)/2 × l
        return((triangle.base * triangle.height / 2) * triangle.length)

myTriangle = Triangle(7, 5)
myTriangle.display()
print("-------------------------------------------")
myTriangularPrism = TriangularPrism(7, 5, 10)
# print("The volume of TriangularPrism is :", TriangularPrism.myTriangularPrism(Triangle))
print("The volume of TriangularPrism is: ", myTriangularPrism.volume())