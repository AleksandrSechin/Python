# Задача №3. В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22 (ввод чисел НЕ в одну строку)
# Output: 32

import math
class1 = int(input("Введите количество учащихся в 1 классе: "))
class2 = int(input("Введите количество учащихся в 2 классе: "))
class3 = int(input("Введите количество учащихся в 3 классе: "))

desk1 = math.ceil(class1 / 2)
desk2 = math.ceil(class2 / 2)
desk3 = (class3 + 1) // 2

print(desk1 + desk2 + desk3)