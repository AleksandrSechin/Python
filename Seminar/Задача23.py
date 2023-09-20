# Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально


import random

rnd = random.randint(5, 10)
print(rnd)
list_1 = []
for _ in range(rnd):
    list_1.append(random.randint(-50, 101))
    list_2 = [random.randint(-50, 101) for _ in range(rnd)]  #
print(list_1)

count = 0
for i in range(len(list_1) - 1):
    if list_1[i] < list_1[i + 1]:
        count += 1
print(count)