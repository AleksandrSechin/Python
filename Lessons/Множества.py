# Множества содержат в себе уникальные элементы, не обязательно упорядоченные. 
# Одно множество может содержать значения любых типов. Если у Вас есть два множества, Вы можете совершать над ними 
# любые стандартные операции, например, объединение, пересечение и разность

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'  удаление значения, ошибка при отсутствии
colors.discard('red') # ok            проверка наличия значения, удаление при наличии, если нет ошибки не будет
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()


a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}           копирование
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединение 
i = a.intersection(b) # i = {8, 2, 5}        пересечение
dl = a.difference(b) # dl = {1, 3}           разность
dr = b.difference(a) # dr = {13, 21}
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут работать методы удаления и добавления
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})
