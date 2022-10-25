numCurr = 1
numPrev = 0
numSum = 1

print("Printing current and previous number sum in a range(10)")
for numCurr, numPrev in range(10):
    print("Current Number" , numCurr, "Previous Number " , numPrev, "Sum: " , numSum)
    numCurr += 1
    numPrev = numCurr - 1
    numSum += 2