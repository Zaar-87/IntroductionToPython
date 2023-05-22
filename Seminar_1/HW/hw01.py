"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

def get_sum_of_digits(number: str) -> int:
    result = 0
    for char in number:
        result += int(char) if char.isdigit() else 0
    return result

number = input('Enter the number:\n')
sum_of_digits = get_sum_of_digits(number)
print('Sum of digits in number', number, 'is', sum_of_digits)