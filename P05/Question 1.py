# create Freshman class
class Freshman:
    # define constructor with name and age as parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # create display method from Freshman class
    def display(self):
        print("Freshman Name =", self.name)
        print("Freshman Age =", self.age)

# create child class MatriculatedStudent of Freshman class
class MatriculatedStudent(Freshman):
    # define constructor of Freshman class with additional parameter, moduleClass
    def __init__(mattress, name, age, moduleClass):
        mattress.name = name
        mattress.age = age
        mattress.moduleClass = moduleClass
  
    # Create display method for MatriculatedStudent class
    def displayMatriculatedStudent(mattress):
        print("Matriculated Student Name =", mattress.name)
        print("Matriculated Student Age =", mattress.age)
        print("Module Class =", mattress.moduleClass)


# Testing Freshman/MatriculatedStudent class
F = Freshman("Chin Chia Ho", 27)
F.display()
print("-------------------------------")
M = MatriculatedStudent("Chin Ho Sei", 28, "1B03")
M.displayMatriculatedStudent()

