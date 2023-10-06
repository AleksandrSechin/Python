# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: print_operation_table(lambda x, y: x * y) 
# Вывод: 
#  1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])

print_operation_table(lambda x, y: x * y)


# Второй вариант
def print_operation_table(operation, num_rows, num_columns):
    x, y = 1, 1
    if num_rows < 2:
        return print('ОШИБКА! Размерности таблицы должны быть больше 2!')

    for x in range(1, num_rows + 1):
        if y == 1:
            print(x, end='')
        else:
            print(operation(x, y), end='')
        for y in range(2, num_columns + 1):
            if x == 1:
                print(' ', end='')
                print(y, end='')
            else:
                print(' ', end='')
                print(operation(x, y), end='')
        if x > 1 and x < num_rows:
            print(' ', end='')
        y = 1
        print('')

# Третий вариант автотеста
def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))