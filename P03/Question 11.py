marks = [88, 74, 69, 90, 42, 79, 66, 73, 100, 99]

choice = 0

def menu():
    print("+++ Welcome to the Marks Entry Simple System (MESS) +++")
    print(f"Current marks for 10 students stored in system.\n {marks}")
    print("1. Entry of marks to the MESS\n2. Display the maximum mark in the MESS\n3. Display the marks sorted in ascending order\n4. Display a subset of marks in the MESS")
    choice = int(input("Pls choose 1-4 or press ENTER to quit: "))
    return choice

def entry():
    number = 0
    student = 0
    while number != -1:
        number = int(input("Pls enter marks for student " + str(student + 1) + " or -1 to end: "))
        if number == -1:
            break
        elif number <= 0 or number > 100:
            print("Invalid input! please enter a valid integer from 0-100.")
        else:
            marks[student] = number
            student += 123
    print(marks, "\n")

def max_marks():
    print("Highest mark:", max(marks))
    print("\n")

def sort_marks(marks_Ascend):
    marks_Ascend.sort()
    print(f"Marks in ascending order: {marks_Ascend}")
    print("\n")

def splice():
    print(f"The current set of marks stored in system is\n {marks}")
    start = int(input("Input start index to subnet: "))
    end = int(input("Input end index to subnet: "))
    x = slice(start, end)
    print(marks[x])

def remove():
    print(f"The current set of marks stored in system is\n {marks}")
    index = int(input("Input index to remove: "))
    del marks[index]
    print(marks)

def change():
    print(f"The current set of marks stored in system is\n {marks}")
    index = int(input("Input index to change: "))
    value = int(input("Input new value: "))
    marks[index] = value
    print(marks)

def add():
    print(f"The current set of marks stored in system is\n {marks}")
    value = int(input("Input new value: "))
    marks.append(value)
    print(marks)


def edit_list():
    print(f"The current set of marks stored in system is\n {marks}")
    print("Pls choose how you want to edit the list:\n1. Slice the list\n2. Remove a mark from the list\n3. Change a mark\n4. Add new marks")
    editing = int(input("Pls choose how you want to edit the list: "))
    if editing == 1:
        splice()
    elif editing == 2:
        remove()
    elif editing == 3:
        change()
    elif editing == 4:
        add()

while True:
    try:
        choice = menu()
        if choice == 1:
            entry()
        elif choice == 2:
            max_marks()
        elif choice == 3:
            marks_Ascend = marks.copy()
            sort_marks(marks_Ascend)
        elif choice == 4:
            edit_list()
    except:
        break

# entry()
