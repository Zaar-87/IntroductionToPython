"""
Задача №17
Дан список чисел. Определите, сколько в нем встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6

Примечание: Пользователь может вводить значения 
списка или список задан изначально.
"""

values_list = [1, 1, 2, 0, -1, 3, 4, 4]

without_duplication = set(values_list)

print(f'At the list {values_list} meets {len(without_duplication)} different meanings')