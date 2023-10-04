# Задача №35. Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым. Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число) Например, числа 2, 3, 5, 7, 11, 13
# Input: 5
# Output: yes

import random


def is_simple_digit(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    for divider in range(3, int((num**0.5) + 1), 2):
        if num % divider == 0:
            return False
        return True


num = int(input("Enter number: "))
if is_simple_digit(num):
    print("yes")
else:
    print("no")
