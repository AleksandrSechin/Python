def sum_number(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa

print(sum_number(5))


# Передать неограниченное кол-во аргументов

def sum_str(*args):
    res = " "
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'r'))
print(sum_str('q', 'e', 'r', 't', 'y'))


#  Модульность - вызов функции из другого файла

import modul1               
print(modul1.max1(5, 9))     

from modul1 import max

import modul1 as m1
print(m1.max1(5, 9))
