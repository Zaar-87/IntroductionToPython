"""
Задача 18
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

import random

length = int(input("Please, enter array size:\n "))
generator_last = int(input("Please, enter maximum number for generator:\n "))
newList = [random.randint(1, generator_last) for _ in range(length)]
print(newList)
number = int(input("Please, enter number to check:\n "))

if newList.count(number) > 0:
    print(f'Number {number} meets {newList.count(number)} time(s)')
elif newList.count(number) == 0:
    number_after = number_before = number
    flag = True
    while (flag):
        number_after += 1
        number_before -= 1
        if number_after in newList:
            print(f'No matches! Nearest number: {number_after}')
            flag = False
        if number_before in newList:
            print(f'No matches! Nearest number: {number_before}')
            flag = False
else:
    print(f'Unknown error!')