"""
Задача №27.
Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих 
подряд, слова разделены одним или большим числом пробелов или символами конца строки. Определите, 
сколько различных слов содержится в этом тексте.

Input: She sells sea shells on the sea shore;The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore,I'm sure that the shells are sea
shore shells.

Output: 19
"""

source_string = "She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."

words = source_string.split(' ')
unique_words = set()
#print(words)

for word in words:
    unique_words.add(word.strip())

num_unique_words = len(unique_words)
print(num_unique_words)