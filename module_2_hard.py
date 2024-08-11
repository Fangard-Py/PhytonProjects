import random

first_stone = []
second_stone = range(1, 20)
rand_num = random.choice([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
first_stone.append(rand_num)
print(first_stone)
for i in first_stone:
    if i == 0:
        continue
    for j in second_stone:
        if i % j == 0:
            print(j)
