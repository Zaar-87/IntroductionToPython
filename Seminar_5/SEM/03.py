"""
Задача №35.
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

Input: 5
Output: yes
"""

n = int(input("Please, Enter the n:\n "))

def number_prime_check(n: int) -> bool:
    for i in range(2, (n // 2) + 1):
        print(f'{i}')
        if n % i == 0:
            return False
    return True

if number_prime_check(n):
    print("This number is prime!")
else:
    print("This number is NOT prime...")