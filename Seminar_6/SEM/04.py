"""
Задача №45. 
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не превосходящее 105.
Программа должна вывести все пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую пару не дает).

Ввод:       Вывод:
300         220 284
"""

# excellent lesson solution!
k = int(input('Please, enter the end of the range:\n '))

def sum_of_dividers(numbers):
    result = 1
    for i in range(2, numbers // 2 + 1):
        if numbers % i == 0:
            result += i
    return result

for i in range(2, k) :
    partner = sum_of_dividers(i)
    if i == sum_of_dividers(partner) and i < partner :
        print(f'{i} - {partner}')

# # my solution
# def find_div_sum(numbers):
#     result = 1
#     for i in range(2, numbers // 2 + 1):
#         if numbers % i == 0:
#             result += i
#             print(result)
#     return result

# def find_div_sum_pairs(k):
#     result = []
#     for i in range(k):
#         second = find_div_sum(i)
#         first = find_div_sum(second)
#         if i == first and i != second and (second, i) not in result:
#             result.append((i, second))
#             print(result)
#     return result

# k = int(input("Please, enter the number:\n "))
# result = find_div_sum_pairs(k)

# print(result)