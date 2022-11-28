noUnit = 0
payAmt = 0
dType = input("Enter the type of dwelling (1-HDB, 2-Condo, 3-Landed): ")
if dType.isalpha():
    print("You have not entered a number")
elif dType > 3:
    pass
else:
    match dType:
        case 1: #HDB
            noUnit = input(input("Enter number of units: "))
            if noUnit > 1000:
                payAmt = noUnit * 0.030
                print(f"Total amount to pay is: {payAmt}")
            elif 501 < noUnit >= 1000:
                payAmt = noUnit * 0.020
                print(f"Total amount to pay is: {payAmt}")
            elif noUnit <=500:
                payAmt = noUnit * 0.010
                print(f"Total amount to pay is: {payAmt}")
        case 2: #Condo
            noUnit = input(input("Enter number of units: "))
            if noUnit > 1000:
                payAmt = noUnit * 0.033
                print(f"Total amount to pay is: {payAmt}")
            elif 501 < noUnit >= 1000:
                payAmt = noUnit * 0.022
                print(f"Total amount to pay is: {payAmt}")
            elif noUnit <=500:
                payAmt = noUnit * 0.011
                print(f"Total amount to pay is: {payAmt}")
        case 3: #Landed
            noUnit = input(input("Enter number of units: "))
            if noUnit > 1000:
                payAmt = noUnit * 0.036
                print(f"Total amount to pay is: {payAmt}")
            elif 501 < noUnit >= 1000:
                payAmt = noUnit * 0.024
                print(f"Total amount to pay is: {payAmt}")
            elif noUnit <=500:
                payAmt = noUnit * 0.012
                print(f"Total amount to pay is: {payAmt}")