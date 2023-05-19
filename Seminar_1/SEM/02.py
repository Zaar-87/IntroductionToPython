"""
Задача №3. Решение в группах
В некоторой школе решили набрать три новых 
математических класса и оборудовать кабинеты для 
них новыми партами. За каждой партой может сидеть 
два учащихся. Известно количество учащихся в 
каждом из трех классов. Выведите наименьшее 
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
"""

from math import ceil

classes_input = int(input('Specify the number of classes:\n'))
pupils_input = [int(input(f'How many pupils are in class № {x + 1}:\n')) 
                for x in range(classes_input)]
desks_count = sum([ceil(x / 2) for x in pupils_input])

print(f'For {classes_input} pupils:\n Summary {sum(pupils_input)} pupils.\n {desks_count} desks needed')