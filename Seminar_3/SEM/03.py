"""
Задача №21
Напишите программу для печати всех уникальных значений в словаре. 

Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII 
": " S007 "}] 
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

dictionary_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

result = []

for item in dictionary_list:
    result.append(list(item.values())[0])
    
print('Counted unique values ->', set(result))

