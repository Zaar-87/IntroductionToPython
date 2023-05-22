"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""

"""Задача 8:
Требуется определить, можно ли от шоколадки размером n × m
долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).

Например:
-   3 2 4 -> yes
-   3 2 1 -> no
"""

def user_input(width=None, length=None, pieces=None):
    width = input('What is the width of the chocolate?\n') if width is None or not width.isdigit() else width
    length = input('What is the length of the chocolate?\n') if length is None or not length.isdigit() else length
    pieces = input('How many slices need to be cut off?\n') if pieces is None or not pieces.isdigit() else pieces
    try:
        width, length, pieces = int(width), int(length), int(pieces)
    except ValueError:
        print('Error! Please, try again:')
        width, length, pieces = user_input(width, length, pieces)
    finally:
        return width, length, pieces

choco_width, choco_length, pieces = user_input()
choco_pieces = choco_width * choco_length
condition_validation = (pieces % choco_width == 0 or pieces % choco_length == 0) and choco_pieces > pieces > 0
print(f'If the chocolate has width = {choco_width} pieces, length = {choco_length} pieces, then you {"COULD" if condition_validation else "COULD NOT"} cut off {pieces} pieces in one break')