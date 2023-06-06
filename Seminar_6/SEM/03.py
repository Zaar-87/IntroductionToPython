"""
Задача №43. 
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных строках.

Ввод:           Вывод:
1 2 3 2 3       2
"""

#our solution
def pairs_count(array):
    count = 0
    for n in set(array):
        count += array.count(n) // 2
    return count

# def read_list_numbers(massive):
#     data = input(massive)
#     return [int(num) for num in data.split(" ")]

#array = read_list_numbers("Please, enter the list of numbers:\n ")

array = [1, 2, 3, 2, 3]
result = pairs_count(array)
print(result)

"""
# lesson solution
arr=[1, 2, 3, 2, 3]
count=0
arr2=[]
for i in range(len(arr)):
    if arr[i] in arr2:
        count+=1
        arr2.remove(arr[i])
    else:
        arr2.append(arr[i])

print(count)
"""