# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

def rhythm(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'а':
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])


stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if rhythm(stroka):
    print('Парам пам-пам')
else:
    print('Пам парам')

# Второе решение
list1 = ['а', 'о', 'е', 'и', 'ы', 'ю', 'я', 'э', 'у', 'я', 'ё']
list2 = stroka.split()
res = []
count = 0
for el1 in list2:
    for el2 in el1:
        if el2 in list1:
            count += 1
    res.append(count)
    count = 0
res_char = res[0]
if all(map(lambda a: a == res_char, res)) and len(res) - 1 > 0:
    print("Парам пам-пам")
elif len(res) - 1 == 0:
    print('Количество фраз должно быть больше одной!')
else:
    print('Пам парам')

# Третье решение автотеста
vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka.split()
if len(phrases) < 2:
    print('Количество фраз должно быть больше одной!')
else:
    countVowels = []

for i in phrases:
    countVowels.append(len([x for x in i if x.lower() in vowels]))

    if countVowels.count(countVowels[0]) == len(countVowels):
        print('Парам пам-пам')
    else:
        print('Пам парам')