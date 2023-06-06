"""
Задача 30: 
Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""

first_element_a = int(input("Please, enter progression 1st elem:\n "))
step_d = int(input("Please, enter progression step_d:\n "))
array_length = int(input("Please, enter progression array_length:\n "))

progression_array = []

current = first_element_a
for n in range(1, array_length + 1):
    current = first_element_a + (n - 1) * step_d
    progression_array.append(current)
 
print(f'Formed progression array -> {progression_array}')