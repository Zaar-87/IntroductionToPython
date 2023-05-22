"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
"""

sum_origamy = input(f'How many cranes the children made?\n')
if sum_origamy.isnumeric() == False or int(sum_origamy) < 6 or int(sum_origamy) % 2 != 0:
    print('Error! The entered value must be a positive number and a multiple to 6!')
elif int(sum_origamy) % 6 == 0: 
    x = int(sum_origamy) // 6
    print(f' Petya made {x}, Katya made {x*4} and Sergej made {x} cranes')
else:
    print('Error! Please try again!') #for ill-conceived options