marks = [80,39,79,81,79,70,84,21,57,66,34,86]

print("The", len(marks), "students scored", marks)
print("Scores that qualify for 'A' grade are: ")

for i in range(len(marks)):
    if(marks[i] >= 80):
        print(marks[i])

def Ascending(marks_Ascend):
    marks_Ascend.sort()
    return marks_Ascend

def Descending(marks_Descend):
    marks_Descend.sort(reverse=True)
    return marks_Descend

def Failed(marks, fail_marks):
    for i in range(len(marks)):
        if(marks[i] < 50):
            (fail_marks.append(i))
        else:
            continue
            
    return fail_marks

fail_marks = []
marks_Descend = marks.copy()
marks_Ascend = marks.copy()

Ascending(marks_Ascend)
Descending(marks_Descend)
Failed(marks, fail_marks)
print(f"a) Marks in ascending order: {marks_Ascend}")
print(f"b) Marks in descending order: {marks_Descend}")
print("c) Highest mark:", max(marks))
print("d) Lowest mark:", min(marks))
print(f"e) Index(es) of students who failed: {fail_marks}")