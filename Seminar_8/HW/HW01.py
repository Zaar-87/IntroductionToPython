"""
Задача 38: 
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""
import functions
import os

def main(file_name):
    while True:
        os.system('CLS')
        functions.drawing()

        user_choice = int(input('Please, select an option: '))

        if user_choice == 1 :
            functions.show_contacts(file_name)
        elif user_choice == 2 :
            functions.add_contact(file_name)
        elif user_choice == 3 :
            functions.change_contact(file_name)
        elif user_choice == 4 :
            functions.delete_contact(file_name)
        elif user_choice == 5 :
            functions.search_contact(file_name)
        elif user_choice == 6 :
            print('\n   Have a nice day!')
            return
        
main('Seminar_8/HW/book.txt')