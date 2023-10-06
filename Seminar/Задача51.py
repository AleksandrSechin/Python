# Задача №51 Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print(‘same’)
# else:
# print(‘different’)
# Вывод: same



def same_by(characteristic, objects):
    for i in range(len(objects)):
        if characteristic(objects[i - 1]) != characteristic(objects[i]):
            return False
    return True

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


# Второй вариант 
def same_by(characteristic, objects):
    res_first_el_char = characteristic(objects[0])
    res_list = list(filter(lambda x: characteristic(x) == res_first_el_char, objects[1:]))
    print(res_list)
    return len(res_list)== len(objects) - 1


values = [0, 2, 7, 8]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')