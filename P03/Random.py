import random

def random_list(total_val, start):
    rand_list = []
    while len(rand_list) < total_val:
        if start == 0 or start == None:
            rand_num = random.randint(start, total_val-1)
        else:
            rand_num = random.randint(start, total_val + (start-1))
        if rand_num not in rand_list:
            rand_list.append(rand_num)
    return rand_list
    

for i in range(3):
    list = random_list(8, 5) # the second argument is optional, default is 0
    print(list)


# for i in range(10):
    
#     print(random.randrange(0, 10), end=" ")