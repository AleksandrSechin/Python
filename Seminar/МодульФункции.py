from modul1 import *
from modul1 import rect, tri


def tri(h, a):
    return 0.5 * h * a


def rect(b, a):
    return b * a


def circle(r):
    return 3.14 * r ** 2


def main():
    print('Начало модуля 1: ')

    print('Начинаем подсчет площади сложной фигуры: ')
    area = rect(20, 30) + tri(10, 20) - circle(5)
    print(area)

    print('Конец модуля 1: ')


if __name__ == "__main__":
    main()

# if __name__ == "__main__":
# print('Начало модуля 1: ')

# print('Начинаем подсчет площади сложной фигуры: ')
# area = rect(20, 30) + tri(10, 20) - circle(5)
# print(area)

# print('Конец модуля 1: ')

# Второй файл

print('Начало модуля 2: ')

area = rect(2, 3) + tri(1, 2)
print(area)

print('Конец модуля 2: ')
