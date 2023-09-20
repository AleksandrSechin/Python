# Задача №19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [3, 4, 5, 1, 2]

k = int(input("Введите число сдвига К: "))
list_1 = [1, 2, 3, 4, 5]
print(list_1[k-1:] + list_1[:k-1])


# Второе решение
k = int(input('Введите число сдвига K: '))
list_1 = [1, 2, 3, 4, 5]
for i in range(len(list_1) - k):
    for j in range(len(list_1) - 1):
        list_1[j], list_1[j - 1] = list_1[j - 1], list_1[j]
print(list_1)


# Третье решение
k = int(input('Введите число сдвига K: '))
list_1 = [1, 2, 3, 4, 5]
for i in range(k):
    list_1.insert(0, list_1.pop())
print(list_1)