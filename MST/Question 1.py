import random

qn_pool = []
list_10 = []
i = 1

while len(qn_pool) < 50:
    qn_pool.append(i)
    i += 1

for i in range(10):
    rand_num = random.randint(qn_pool[0], len(qn_pool))
    if rand_num % 2 == 0:
        if rand_num in list_10:
            rand_num = random.randint(qn_pool[0], len(qn_pool))
        else:
            list_10.append(rand_num)
print(list_10)