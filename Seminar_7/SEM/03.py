"""
Задача №51.
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение 
некоторой характеристики, и возвращают True, если это так. 
Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция 
должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

Ввод: 
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)

Вывод:
same
"""

values = [1, 2, 3, 4, 5]

def same_by(f, items):
    for item in items:
        if not f(item):
            return False
    return True

result = same_by(lambda x: x % 2 == 0, values)
print(result)

"""
# not optimal
def same_by(characteristic, objects):
    new = list(filter(characteristic, objects))
    return len(new) == len(objects)
"""