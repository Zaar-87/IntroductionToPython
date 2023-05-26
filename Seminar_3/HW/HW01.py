"""
Задача 16 
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    3
    -> 1
"""

import random

length = int(input("Please, enter array size:\n "))
generator_last = int(input("Please, enter maximum number for generator:\n "))
newList = [random.randint(1, generator_last) for _ in range(length)]
print(f'Array: {newList}')
num = int(input("Please, enter number to check:\n "))

if newList.count(num) > 0:
    print(f'Number {num} meets {newList.count(num)} time(s)')
elif newList.count(num) == 0:
    print(f'Sorry! no matches!')
else:
    print(f'Unknown error')