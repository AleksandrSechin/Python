list_1 = [] # Создание пустого списка
list_2 = list() # Создание пустого списка
list_1 = [7, 9, 11, 13, 15, 17]

list_1 = [7, 9, 11, 13, 15, 17]
print(list_1[0]) # 7
print(list_1[-1]) # 17

list_1 = [7, 9, 11, 13, 15, 17]  # узнать количество элементов в списке функция len(имя_списка)
print(len(list_1)) # 6

list_1 = list() # создание пустого списка
for i in range(5): # цикл выполнится 5 раз
    list_1.append(i) # сохранение элемента в конец списка
# 1-я итерация цикла(повторение 1): n = 12, list_1 = [12]
# 2-я итерация цикла(повторение 2): n = 7, list_1 = [12, 7]
# 3-я итерация цикла(повторение 3): n = -1, list_1 = [12, 7, -1]
# 4-я итерация цикла(повторение 4): n = 21, list_1 = [12, 7, -1, 21]
# 5-я итерация цикла(повторение 5): n = 0, list_1 = [12, 7, -1, 21, 0]
print(list_1) # [12, 7, -1, 21, 0]

list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) # 0
print(list_1) # [12, 7, -1, 21]

list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12
print(list_1) # [7, -1, 21, 0]

list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))
print(list_1) # [12, 7, 11, -1, 21, 0]

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) #[9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]



# Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]
# Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),..., (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]


# Копирование списков и их изменение
import copy

my_list = [111, 222, 333, 444, 555]

my_list_1 = my_list

my_list_1[2] = 0

print(my_list)
print(my_list_1)
print()
my_list_2 = my_list.copy()

my_list_2[2] = 999

print(my_list)
print(my_list_2)
print()

my_list.append([123,234,345])
my_list_3 = my_list.copy()
print(my_list)
print(my_list_3)
print()

my_list_3[2] = 100
my_list_3[-1][1] = 200
print(my_list)
print(my_list_3)
print()


my_list_4 = copy.deepcopy(my_list)
print(my_list)
print(my_list_4)
print()

my_list_4[2] = '*****'
my_list_4[-1][1] = '~~~~~~'
print(my_list)
print(my_list_4)
print()

my_tuple = (123,234,456,678, [100, 200, 300])
print(my_tuple)
my_tuple[-1][-1] = 999999
print(my_tuple)