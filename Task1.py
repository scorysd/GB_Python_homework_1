# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
day = input('Введите номер, обозначающий день недели:')
day = int(day)
if day == 6 or day == 7:
    print('Выходной')
elif day <= 0 or day > 7:
    print('Такого дня недели не существует')
else:
    print('Не выходной')