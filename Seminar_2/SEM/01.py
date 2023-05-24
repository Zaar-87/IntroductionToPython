"""
Задача №9.
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
"""

n = int(input("Please, enter the number: "))
temp = 1
sum = 1
while temp<=n:
    sum = sum * temp
    temp += 1
print(f'Product of numbers is: {sum}')
