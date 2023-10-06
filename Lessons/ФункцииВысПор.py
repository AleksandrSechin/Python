def calk1(a, b):     
    return a + b 

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calk1, 5, 6)
math(calk2, 5, 6)


# Сокращение функции
def math(op, x, y):
    print(op(x, y))
calk1 = lambda a,b: a + b  # 17 перенос в 18
math(calk1, 5, 6)          # math(lambda a,b: a + b , 5, 6)


# Задача. Выбрать четные числа и составить список пар (число, квадрат числа)
data = [1, 2, 3, 5, 8, 15, 23]
res = list()
for i in data:
    if i % 2 == 0:
        res.append((i, i**2))
print(res)

# # Вариант с lambda
def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)


# Функция map меняет значение для каждого элемента списка
list_1 = [x for x in range(1, 10)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

# Задача. Превратить строку в список чисел
# Функция строка.split() убирает все пробелы и создает список из значений строки
data = '1 2 3 5 8 15 23'
data = list(map(int, data.split()))
print(data)   # [1, 2, 3, 5, 8, 15, 23]

# Функция filter() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с теми объектами, для которых
# функция вернула True

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)  # [15, 65, 175]

# Итог 
data = [1, 2, 3, 5, 8, 15, 23]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)