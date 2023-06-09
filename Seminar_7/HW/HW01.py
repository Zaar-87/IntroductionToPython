"""
Задача 34: 
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

Ввод: 
пара-ра-рам рам-пам-папам па-ра-па-дам

Вывод:
Парам пам-пам
"""

vowels_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ы', 'ю', 'я']

# vinnies_poem = 'пара-рам рам-пам-пап па-ра-па-да'
vinnies_poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'
phrase_list = vinnies_poem.split(' ')
print(f'Vinnies poem consists of the following sequence -> {phrase_list}')

def vowels_counting(list1, list2):
    count = 0
    count_list = []
    for word in list1:
        for letter in word:
            if letter in list2:
                count += 1
        count_list.append(count)
        count = 0
    return count_list

def rhyme_check(check_list):
    if len(check_list) == len(list(filter(lambda x: x == check_list[0], check_list))):
        return 'Good! "Парам пам-пам"'
    else:
        return 'Too bad... "Пам парам"'

number_of_vows = vowels_counting(phrase_list, vowels_list)
print(f'We have such subsequence number of syllables -> {number_of_vows}')
result = rhyme_check(vowels_counting(phrase_list, vowels_list))
print(result)