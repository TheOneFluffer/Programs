marks = [80,39,79,81,79,70,84,57,66,86]
marks = marks.split(sep = ",")
print(f"The 10 students scored {marks}. \tMarks that qualify for 'A' grade are:\n")
for i in marks:
    if (marks >= 80):
        print(i)