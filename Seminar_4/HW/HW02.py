"""
Задача 24. 
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.

В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
"""

#Т.к. задача относительно несложная, здесь я попробовал заморочиться с проверками. Возможно в данном случае что-то оказалось избыточным, но решил попробовать разобраться в вариантах отладки

import random

def user_input(generator_min=None, generator_max=None, bushes_quantity=None):
    generator_min = input('Please, enter minimum number for berries generator:\n ') if generator_min is None or not generator_min.isdigit() else generator_min
    generator_max = input('Please, enter maximum number for berries generator:\n ') if generator_max is None or not generator_max.isdigit() else generator_max
    bushes_quantity = input('Please, enter quantity of bushes:\n ') if bushes_quantity is None or not bushes_quantity.isdigit() else bushes_quantity
    try:
        generator_min, generator_max, bushes_quantity = int(generator_min), int(generator_max), int(bushes_quantity)
    except ValueError:
        print('Error! Please, try again:')
        generator_min, generator_max, bushes_quantity = user_input(generator_min, generator_max, bushes_quantity)
    finally:
        return generator_min, generator_max, bushes_quantity

generator_min, generator_max, bushes_quantity = user_input()

if bushes_quantity <= 2:
    print('Error! Quantity of the bushes must be > 2!')
elif generator_min <= 0 or generator_max <= 0:
    print('Error! Quantity of berries cannot be a negative number!')
elif generator_min > generator_max:
    print('Error! Minimum number for berries generator must be less or equal to maximum number for berries generator!')
else:        
    ridge_file = [random.randint(generator_min, generator_max) for _ in range(bushes_quantity)]
    print(f'Our ridge looks like this:\n {ridge_file}')

    max_berries = 0
    for i in range(bushes_quantity):
        j = 0 if i + 1 == bushes_quantity else i + 1
        sum = ridge_file[i] + ridge_file[j] + ridge_file[i-1]
        if sum > max_berries:
            max_berries = sum
            optimum_bush_index = i
    print(f'Module will pick {max_berries} berries and for this it must begin from the bush placed on {optimum_bush_index + 1} position')