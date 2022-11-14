def select_difficulty():
    isTrue = True
    while isTrue:
        try:
            print("\nSelect difficulty level:\n  [1]Easy\n  [2]Standard\n  [3]Hard\n")
            selection = input('Enter choice: ')
            selection = int(selection)
            match selection:
                case 1:
                    tries = 10
                    break
                case 2:
                    tries = 5
                    break
                case 3:
                    tries = 3
                    isTrue = False
                case _:
                    print("Please type in a selection within 1 to 3!")
                    return tries
        except:
            print("Pls enter a number")

print_me = select_difficulty()
print(print_me)