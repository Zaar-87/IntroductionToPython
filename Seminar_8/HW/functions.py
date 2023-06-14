import os
from time import sleep

delay_short = 3 # global delay (short) timing
delay_long = 5 # global delay (long) timing

# Outputing all information from the directory
def show_contacts(file_name) -> None:
    os.system('CLS')
    with open(file_name, 'r', encoding="utf-8") as file:
        contacts = file.readlines()
    
        for contact in contacts:
            print(contact, end='')
    input('\n\n   press ENTER to return to main menu')

# Adding new information
def add_contact(file_name) -> None:
    os.system('CLS')
    surname_contact = str.title(input('Input a surname of contact: ') + ' ')
    name_contact = str.title(input('Input a name of contact: ') + ' ')
    phone_contact = input('Input a phone number of contact: ')
    contact = surname_contact + name_contact + phone_contact
    print(f'Do you want add this contact to directory:\n{contact}')
    check = input('Press "y" to continue / Press ENTER to abort\n')
    if check == 'y':
        with open(file_name, 'r+', encoding='UTF-8') as contacts:
            target = contacts.readlines()
            count = len(target)
            contact = '\n' + str(count) + " " + contact
            contacts.write(contact)
            print('Operation successful')
            sleep(delay_short)
    else:
        input('\n   Operation aborted!\n\n   press ENTER to return to main menu')            

# Finding entries
def search_contact(file_name) -> None:
    os.system('CLS')
    target = str.title(input('Input target for searching: '))

    with open(file_name, 'r', encoding="utf-8") as file:
        contacts = file.readlines()

        for contact in contacts:                
            if target in contact:
                print(contact)
                break
        else :
            print('No match!')
    input('\n   press ENTER to return')

# Changing contact
def change_contact(file_name) -> None:
    os.system('CLS')
    with open(file_name, 'r', encoding="utf-8") as file:
        contacts = file.readlines()
        count = len(contacts)

    target = input('Input contact for correcting: ')
    index_line = string_number_finding(contacts, target)
    if index_line == 0:
        print('You have found elements that cannot be modified :)\n Please, change search criteria')
        sleep(delay_long)
        change_contact(file_name)
    elif index_line < 0 or index_line > count: # for 'index_line > count' no case in this solution. this is only for further sols
        print('Searched contact not found!')
        sleep(delay_short)
        return
    else:
        with open(file_name, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            count = len(lines)
        if index_line > 0 and index_line <= count:
            print(f'Do you want change fields of this contact?\n')
            check = input('Press "y" to continue / Press ENTER to abort\n')
            if check == 'y':
                print('Enter parameter that you want to change\n' +
                    '1. Surname 2. Name 3. Telephone 4. Abort')
                num = input()
                if num == "1":
                    new_surname = input('Enter new surname: ')
                    item = lines[index_line].split()
                    item[1] = new_surname
                    lines[index_line] = ' '.join(item) + "\n"
                    with open(file_name, 'r+', encoding='UTF-8') as file:
                        file.write("№ Surname Name Telephone\n")
                        for i in range(1, count):
                            file.write(lines[i])
                    print('Operation successful')
                    sleep(delay_short)
                elif num == "2":
                    new_name = input('Enter new name: ')
                    item = lines[index_line].split()
                    item[2] = new_name
                    lines[index_line] = ' '.join(item) + "\n"
                    with open(file_name, 'r+', encoding='UTF-8') as file:
                        file.write("№ Surname Name Telephone\n")
                        for i in range(1, count):
                            file.write(lines[i])
                    print('Operation successful')
                    sleep(delay_short)                            
                elif num == "3":
                    new_phone = input('Enter new phone: ')
                    item = lines[index_line].split()
                    item[3] = new_phone
                    lines[index_line] = ' '.join(item) + "\n"
                    with open(file_name, 'r+', encoding='UTF-8') as file:
                        file.write("№ Surname Name Telephone\n")
                        for i in range(1, count):
                            file.write(lines[i])
                    print('Operation successful')
                    sleep(delay_short)
                else:
                    input('\n   Operation aborted!\n\n   press ENTER to return to main menu')
            else:
                input('\n   Operation aborted!\n\n   press ENTER to return to main menu')  
        else:
            print('Error! Please try again.\n')

# Deleting contact
def delete_contact(file_name) -> None:
    os.system('CLS')
    target = input('Input contacts for deleting: ')
    with open(file_name, "r", encoding="utf-8") as file:
        contacts = file.readlines()    
    index_line = string_number_finding(contacts, target)
    if index_line == -1:
        print('Sorry, no contact found by entered criteria!')
        sleep(delay_short)
        print('Do you want continue?\n')
        check = input('Press "y" to continue / Press ENTER to abort\n')
        if check == 'y':
            delete_contact(file_name)
        else:
            input('\n   Operation aborted!\n\n   press ENTER to return to main menu')      
    else:
        print(f'Do you really want delete this contact from the directory?\n')
        check = input('Press "y" to continue / Press ENTER to abort\n')
        if check == 'y':
            contacts.pop(index_line)
            with open(file_name, "w", encoding="utf-8") as file:
                file.writelines(contacts, )
                print('Operation successful')
                sleep(delay_short)
        else:
            input('\n   Operation aborted!\n\n   press ENTER to return to main menu')             

# Finding number of string and printing found string (additional func for delete and change functions)
def string_number_finding(file: list[str], target: str) -> int:
    target = target.lower()
    for i in range(len(file)):
        if target in file[i].lower():
            print(file[i])
            return i
    return -1  
 
# Interface
def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - change contact')
    print('4 - delete contact')
    print('5 - search contact')
    print('6 - exit')