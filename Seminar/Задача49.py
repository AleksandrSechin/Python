# Задача №49. Дан список размеров(длина, ширина) эллипсов
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого эллипса и возвращает кортеж с его размерами.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
# - Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
# При решении задачи используйте списочные выражения.
# Гарантируется, что самый большой эллипс всего один.
# Ввод: orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод: 2.5 10


def find_farthest_orbit(list_of_orbits):
    sizes = list(filter(lambda item : item[0] != item[1], list_of_orbits))
    areas = list(map(lambda item : 3.14 * item[0] * item[1], sizes))
    maximum = areas[0]
    imax = 0
    for i, area in enumerate(areas[1:], 1):
        if area > maximum:
            maximum = area # maximum = max(maximum, area)
            imax = i
    return sizes[imax]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))