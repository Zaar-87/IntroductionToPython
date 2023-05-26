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
num = int(input("Please, enter number to check:\n "))

if newList.count(num) > 0:
    print(f'Number {num} meets {newList.count(num)} time(s)')
elif newList.count(num) == 0:
    numR = numL = num
    flag = True
    while (flag):
        numR += 1
        numL -= 1
        if numR in newList:
            print(f'No matches! Nearest number: {numR}')
            flag = False
        if numL in newList:
            print(f'No matches! Nearest number: {numL}')
            flag = False
else:
    print(f'Unknown error')