"""
Задача 32:
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного максимума)

1-й пример
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

Вывод: [1, 9, 13, 14, 19]

2-й пример
Ввод: [10, 25, 7, 23, 45]
начальное значение: 20
конечное значение: 40
Вывод: [1, 3]
"""

import random

array_length = int(input("Please, enter array length for generation:\n "))
array = [random.randint(-10, 10) for _ in range(array_length)]

print(array)

range_start = int(input("Please, enter start number of the range:\n "))
range_end = int(input("Please, enter end number of the range:\n "))

array_indices = []
for i in range(array_length):
    if array[i] >= range_start and array[i] <= range_end:
        array_indices.append(i)

print(f'Formed array with matching to conditions indices -> {array_indices}')