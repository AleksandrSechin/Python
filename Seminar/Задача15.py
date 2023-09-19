# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один дл
# я себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и
#  он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

# Николай Мануилов 2) Пользователь вводит одно число N. Далее идут N чисел,
#  записанных на новой строчке каждое. Вывести максимальное и минимальное (циклы)
# Input: 5 -> 5 1 6 5 9
# Output: 1 9


import random


num = random.randint(5, 10)
min_num_kg = 1000
max_num_kg = -1000
for i in range(num):
    kg = random.randint(1, 15)
    if kg < min_num_kg:
        min_num_kg = kg
    elif kg > max_num_kg:
        max_num_kg = kg
print(min_num_kg)
print(max_num_kg)


# Второй вариант
import random


num = random.randint(5, 10)
kg = random.randint(1, 15)
min_num_kg = kg
max_num_kg = kg
for _ in range(num - 1):
    kg = random.randint(1, 15)
    if kg < min_num_kg:
        min_num_kg = kg
    elif kg > max_num_kg:
        max_num_kg = kg
print(min_num_kg)
print(max_num_kg)