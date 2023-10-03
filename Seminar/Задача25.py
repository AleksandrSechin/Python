# Задача 25. Напишите программу, которая принимает на вход строку, и
# отслеживает, сколько раз каждый символ уже встречался. Количество
# повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

list1 = "a a a b c a a d c d d".split()
list1.reverse()
print(list1)
for i in range(len(list1)):
    list1[i] = f'{list1[i]}_{list1.count(list1[i]) - 1}'
list1.reverse()
list1 = " ".join(list1)
list1 = list1.replace("_0", "")
print(list1)


# Второй вариант
list1 = "a a a b c a a d c d d".split()
dict1 = {}

for el in list1:
    if el in dict1:
        dict1[el] += 1
        print(f'{el}_{dict1[el]}', end=" ")
    else:
        dict1[el] = 0
        print(el, end=" ")
