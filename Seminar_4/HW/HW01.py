"""
Задача 22.
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""

import random

generator_min = int(input("Please, enter minimum number for generator:\n "))
generator_max = int(input("Please, enter maximum number for generator:\n "))

list_length_1 = int(input("Please, enter first list size:\n "))
disordered_list_1 = [random.randint(generator_min, generator_max) for _ in range(list_length_1)]
print(disordered_list_1)
sorted_list_1 = set(disordered_list_1)

list_length_2 = int(input("Please, enter second list size:\n "))
disordered_list_2 = [random.randint(generator_min, generator_max) for _ in range(list_length_2)]
print(disordered_list_2)
sorted_list_2 = set(disordered_list_2)

result = sorted(sorted_list_1.intersection(sorted_list_2))

print(f'The numbers that occur in both lists are -> {result}')