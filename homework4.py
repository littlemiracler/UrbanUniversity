print('Практическая работа по уроку "Организация программ и методы строк."')
print("_____________________________________________________________")
my_string = input('Введите любую фразу: ')
print("В Вашей фразе", len(my_string), "символа(ов), учитывая пробелы.")
print('Ваша фраза в верхнем регистре: ', my_string.upper())
print('Ваша фраза в нижнем регистре: ', my_string.lower())
new_my_string = my_string.replace(' ', '')
print('Ваша фраза без пробелов: ', new_my_string)
print("Первая буква в Вашей фразе: ", new_my_string[0])
print("Последняя буква в Вашей фразе: ", new_my_string[-1])