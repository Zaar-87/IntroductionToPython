"""
Задача №33.
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

grades = [5, 2, 3, 2, 4, 2, 5, 5, 2]
print(f'Original: {grades}')

def replacing_max_and_min(array: list[int]):
    min_number = min(array)
    max_number = max(array)

    for i in range(len(array)):
        if array[i] == max_number:
            array[i] = min_number

replacing_max_and_min(grades)
print(f'Modificated: {grades}')