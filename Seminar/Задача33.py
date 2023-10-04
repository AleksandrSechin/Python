# Задача №33. Хакер Василий получил доступ к классному журналу и хочет
# заменить все свои минимальные оценки на максимальные. Напишите
# программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint
import time

start = time.time()


def invertMaxMarks(marks):
    max_mark, min_mark = max(marks), min(marks)
    for i in range(len(marks)):
        if marks[i] == max_mark:
            marks[i] = min_mark
    return marks


n = randint(5, 10)
marks = [randint(1, 5) for _ in range(n)]
print(marks)
print(invertMaxMarks(marks))
end = time.time()
print(end - start)


# Второй вариант

def invertMaxMarks(marks):
    max_mark = min_mark = marks[0]
    index_max_mark = [0]
    for i in range(len(marks)):
        if marks[i] > max_mark:
            max_mark = marks[i]
            index_max_mark = [i]
        elif max_mark == marks[i]:
            index_max_mark.append(i)
        if marks[i] < min_mark:
            min_mark = marks[i]
    for i in index_max_mark:
        marks[i] = min_mark
    return marks


n = randint(5, 10)
marks = [randint(1, 5) for _ in range(n)]
print(marks)
print(invertMaxMarks(marks))
