#  Модульность - вызов функции из другого файла

import modul1
import modul1 as m1
from modul1 import *  # импорт всех функций модуля

print(modul1.max1(5, 9))
# или
print(m1.max1(5, 9))

# Функции


def sum_number(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
    print(stop)  # не выводится после return


print(sum_number(5))
# или
a = sum_number(5)
print(a)


def max1(a, b):
    if a > b:
        return a  # return прерывает, else не используется
    return b


# Передать неограниченное кол-во аргументов (*args)

def sum_str(*args):
    res = " "
    for i in args:
        res += i
    return res


print(sum_str('q', 'e', 'r'))
print(sum_str('q', 'e', 'r', 't', 'y'))
