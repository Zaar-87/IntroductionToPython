"""
Задача 14:
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

Например:
Input:
10
Output:
1 2 4 8
"""

input_number = int(input('Please, enter a number:\n'))

k = 0
while 2 ** k <= input_number:
    print(2 ** k, end=', ')
    k += 1