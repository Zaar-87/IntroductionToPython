"""
Задача №41.
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве. Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.

Ввод:           Ввод:
5 1 2 3 4 5     5 1 5 1 5 1     
Вывод:          Вывод:
0               2
(каждое число вводится с новой строки)
"""

def count_lower_neighbor(list):
    count = 0
    for item in range(1, len(list) - 1):
        if list[item] > list[item - 1] and list[item] > list[item + 1]:
            count += 1
    return count

# def read_list_numbers(massive):
#     data = input(massive)
#     return [int(num) for num in data.split(" ")]

# list = read_list_numbers("Please, enter the list of numbers:\n ")

list = [5, 1, 2, 3, 4, 5]
list = [5, 1, 5, 1, 5, 1 ]

result = count_lower_neighbor(list)
print(result)