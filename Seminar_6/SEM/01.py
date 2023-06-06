"""
Задача №39.
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

Ввод:               Вывод:
3 1 3 4 2 4 12      3 3 2 12

4 15 43 1 15 1 

каждое число вводится с новой строки
"""

def get_queue_unique_values(array_1, array_2):
    result_sequence = []
    for number in array_1:
        if number not in array_2:
            result_sequence.append(number)
    return result_sequence

# def read_list_numbers(massive):
#     data = input(massive)
#     return [int(number) for number in data.split(" ")]

# list_1 = read_list_numbers("Please, enter the first list of numbers:\n ")
# list_2 = read_list_numbers("Please, enter the second list of numbers:\n ")

list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1]

result_sequence = get_queue_unique_values(list_1, list_2)

print(result_sequence)