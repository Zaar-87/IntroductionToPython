"""
Задача №19
Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на K элементов вправо, K – положительное число.

Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

input_list = [1, 2, 3, 4, 5]

n = int(input("Please, specify the shift: ")) % len(input_list)
for i in range(n):
    input_list.insert(0, input_list.pop())
    
print(input_list)

# second var

# k = int(input('Please, specify the shift:\n'))
# input_data = [1, 2, 3, 4, 5]
# length = len(input_data)
# k = k % length
# print(input_data[-k:] + input_data[:-k])