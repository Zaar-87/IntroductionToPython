# """
# Задача №25.
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()
# """

# 1st (seminar) var
text = 'a a a b c a a d c d d'

my_list = text.split()
n = ''
dict={}

for i in my_list:
    if i in dict.keys():
        dict[i]+=1
        n +=f'{i}_{dict[i]} '
    else:
        dict[i]=0
        n+=f'{i} '
#    print(dict)
print(n)

# 2nd (my) var
# my_list = 'a a a b c a a d c d d'

# letters = {}
# result = ''

# for letter in my_list.split(' '):
#     number = letters.get(letter)
#     if number is None:
#         letters[letter] = 1
#         result += letter + ' '
#     else:
#         result += f'{letter}_{number} '
#         letters[letter] += 1

# print(result)