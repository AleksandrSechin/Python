# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные друг другу
# образуют одну пару, которую необходимо посчитать. Вводится список чисел.
# Все числа списка находятся на разных строках
# Ввод: 1 2 3 2 3
# Вывод: 2

from random import randint

n = randint(5, 10)
list1 = [randint(1, 10) for _ in range(n)]
print(list1)

count = 0

for i in range(len(list1) - 1):
    for j in range(i + 1, len(list1)):
        if list1[i] == list1[j]:
            count += 1
print(count)


# Пример с компрехеншн

list1 = [1, 2, 3, 2, 3, 2, 2]
print(list1)

count = 0

for i in range(len(list1) - 1):
    for j in range(i + 1, len(list1)):
        if list1[i] == list1[j]:
            count += 1
print('результат первого решения: ', count)

count_list = []
for i in range(len(list1) - 1):
    for j in range(i + 1, len(list1)):
        if list1[i] == list1[j]:
            count_list.append(1)
print('результат второго решения: ', sum(count_list))

res = sum([1 for i in range(len(list1) - 1)
          for j in range(i + 1, len(list1)) if list1[i] == list1[j]])
print('результат третьего решения: ', res)
