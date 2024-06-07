print('Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"')
print("_____________________________________________________________")
immutable_var = 23, 'food', 'lesson', True
print(immutable_var)
#immutable_var[0] = 32
#print(immutable_var)
# Ошибка: TypeError: 'tuple' object does not support item assignment
# т.к. Кортеж ('tuple') неизменяемый обьект
mutable_list = [23, 'food', 'lesson', True]
mutable_list[0] = 32
print(mutable_list)