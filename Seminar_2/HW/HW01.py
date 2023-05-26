"""
Задача 10:
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть

Например:
Input:
5 -> 1 0 1 1 0
Output:
2
"""

import random

num = random.randint(2, 8)
print(f'On the table lies {num} coins')
tails = 0
eagle = 0
for i in range(num):
    side = random.randint(0, 1)
    if side == 0: 
        eagle += 1
    else:
        tails += 1
    print(side, end=' ')
print (f'\nThe minimum number of flips in this situation -> {eagle if eagle < tails else tails}')
