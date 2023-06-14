"""
Задача №49.
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""
import functions
import os

def main(file_name):
    while True:
        os.system('CLS')
        functions.drawing()

        user_choice = int(input('Please, select an action option: '))

        if user_choice == 1 :
            functions.show_contacts(file_name)
        elif user_choice == 2 :
            functions.add_contact(file_name)
        elif user_choice == 3 :
            functions.search_contact(file_name)
        elif user_choice == 4 :
            print('\n   Have a nice day!')
            return
        
main('Seminar_8/SEM/book.txt')