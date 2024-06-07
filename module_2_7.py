print('Самостоятельная работа по уроку "Распаковка параметров и параметры функции"')
print("___________________________________________________________________________")
print('1.Функция с параметрами по умолчанию:')
print('  ')


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
print('------')
print('2.Распаковка параметров:')
print('  ')


def values_list(a=1, b='строка', c=True):
    print(a, b, c)


values_dict = [12, 'список', False]
values_list(*values_dict)

print('------')
print('3.Распаковка + отдельные параметры:')
print('  ')

values_list_2 = (15, 'Лес')
print_params(*values_list_2, 42)

print("______________________________________________________________________________________")
print('Самостоятельная работа по уроку "Распаковка параметров и параметры функции": выполнена')