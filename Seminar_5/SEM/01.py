"""
Задача №31
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи

Input: 7
Output: 13
Задание необходимо решать через рекурсию
"""
import custom_func

print(f"The fibonacci number is -> {custom_func.last_fibon}")

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     if n in [1, 2]:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# num = int(input("Enter the fibonacci number:\n "))
# fibonacci_number = fibonacci(num)

# print(f"The fibonacci number is -> {fibonacci_number}")