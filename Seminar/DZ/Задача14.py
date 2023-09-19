# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8


n = input("Введите число: ")
while not n.isdigit():
    print("Вы ввели не число")
    n = input("Введите число: ")
n = int(n)
degree = 0
while 2 ** degree <= n:
    print(2 ** degree)
    degree += 1