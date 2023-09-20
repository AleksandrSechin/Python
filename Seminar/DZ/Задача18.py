# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random


n = int(input("Введите количество элементов: "))
list_1 = [random.randint(1, 10) for num in range(n)]
print(*list_1)
x = int(input("Введите число Х: "))
min_dif = abs(list_1[0] - x)
lst = list_1[0]
for num in list_1[1:]:
    dif = abs(num - x)
    if dif < min_dif:
        min_dif = dif   # min_dif = min(min_dif, dif) функция поиска минимума
        lst = [num]
    # elif dif == min_dif and num not in lst:
    #     lst.append(num)
print(*lst)