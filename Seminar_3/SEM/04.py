"""
Задача №23
Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество 
элементов массива, больших предыдущего (элемента с предыдущим номером) 

Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""

array = [0, -1, 5, 2, 3, 8, 9, 2]

counter = [1 for x in range(1, len(array)) if array[x - 1] < array[x]]

print(f'In array {array} -> {sum(counter)} elements are bigger than previos of them.')