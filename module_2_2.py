print('Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."')
print("_____________________________________________________________")
print("Введите, пожалуйста, три числа:")
first = int(input('1: '))
second = int(input('2: '))
third = int(input('3: '))
if first == second and first == third and second == third:
    print('3 одинаковых числа')
elif first == second or first == third or second == third:
    print('2 одинаковых числа')
else:
    print('Нет одинаковых чисел')
print("_____________________________________________________________")
print('Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else.": выполнена')