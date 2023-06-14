import os

# Outputs information from the directory
def show_contacts(file_name) -> None:
    os.system('CLS')
    with open(file_name, 'r', encoding="utf-8") as file:
        data = file.readlines()

        for contact in data:
            print(contact, end='')
    input('\n   press any key')

# Adds information to the directory
def add_contact(file_name) -> None:
    os.system('CLS')
    with open(file_name, 'a', encoding="utf-8") as file:
        res = ''
        res += input('Input a surname of contact: ') + ' '
        res += input('Input a name of contact: ') + ' '
        res += input('Input a phone number of contact: ')

        file.write('\n'+ res)    
    input('Contact was successfully added! \n Press ENTER to return')

# Finds entries by a specific search criteria
def search_contact(file_name) -> None:
    os.system('CLS')
    target = input('Input info for searching: ')

    with open(file_name, 'r', encoding="utf-8") as file:
        contacts = file.readlines()

        for contact in contacts:                
            if target in contact:
                print(contact)
                break
        else :
            print('No match!')
    input('\n   Press ENTER to return')

# Interface
def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - search contact')
    print('4 - exit')