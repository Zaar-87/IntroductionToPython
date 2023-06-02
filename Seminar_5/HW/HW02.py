"""
Задача 28: 
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

2 2
4
"""

a = int(input("Please, enter the number a:\n "))
b = int(input("Please, enter the number b:\n "))

def sum(a, b):
    if a == 1:
        return a + b
    else:
        print(a,b)
        return sum(a - 1, b) + 1

print(f'Result -> {sum(a, b)}')