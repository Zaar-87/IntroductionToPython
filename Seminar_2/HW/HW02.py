"""
Задача 12:
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

Например:
Input:
1. 4 4 ->
2. 5 6 ->
Output:
1. -> 2 2
2. -> 2 3
"""

sum_of_numbers = int(input("Please, enter sum of numbers: "))
product_of_numbers = int(input("Please, enter product of numbers "))

flag = True
x = 0
y = 0

for i in range(2, 1001):
    for j in range(2, 1001):
        if i + j == sum_of_numbers and i * j == product_of_numbers:
            flag = False
            x = i
            y = j
            break
        else:
            j += 1
    if flag == False:
        break
    else:
        i += 1

print(f"x = {x}, y = {y}")
