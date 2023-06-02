"""
Задача №37.
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.

Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

Input: 2 -> 3 4
Output: 4 3
"""

count_numbers = int(input("Please, enter the count of numbers (N):\n "))

def reverse_numbers(count_numbers: int):
    user_number = int(input("Please, enter the number: "))
    if count_numbers > 1:
        reverse_numbers(count_numbers - 1)
    print(user_number, end = ' ')

reverse_numbers(count_numbers)

# n = int(input("Enter the number "))

# def spinPrint(x):
#     a = int(input("Enter the number "))
#     if x > 1 :
#         spinPrint(x-1)  
#     print(a)
    
# spinPrint(n)