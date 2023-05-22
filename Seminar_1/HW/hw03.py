"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
"""

def ticket_is_lucky(ticket_number: str) -> bool:
        length = len(ticket_number)
        middle = length // 2
        if length % 2 == 0:
            left_side, right_side = ticket_number[:middle], ticket_number[middle:]
        else:
            left_side, right_side = ticket_number[:middle], ticket_number[middle + 1:]
        return sum([int(i) for i in left_side]) == sum([int(i) for i in right_side])

ticket_number = input(f'Enter the ticket number:\n')
if ticket_number.isnumeric() == False:
    print('Error! The entered value must be only a positive number!')
elif ticket_number.isnumeric() == True:
    lucky = ticket_is_lucky(ticket_number)
    print(f'Ticket №{ticket_number} -> {"Hooray! Ticket is lucky!" if lucky else "Oops... This ticket is not lucky("}')
else:
    print('Error! Please try another variant!') #for ill-conceived options