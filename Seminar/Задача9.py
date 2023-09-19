# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 
# 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

n = input("Введите целое число N: ")

while not n.isdigit():
    print("Вы ввели не число")
    n = input("Введите целое число N: ")

n = int(n)
fact = 1

while n > 1:
    fact *= n
    n -= 1

print(fact)


# Вариант 2
n = input("Введите целое число N: ")

while not n.isdigit():
    print("Вы ввели не число")
    n = input("Введите целое число N: ")

n = int(n)
mult = 1
fact = 1

while mult <= n:
    fact *= mult
    mult += 1
print(fact)