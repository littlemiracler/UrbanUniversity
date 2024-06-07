print('Дополнительное практическое задание по модулю: "Основные операторы"')
print("_______________________________________________________________________________")
'''num = int(input("Введите число от 3 до 20: "))
pairs = []

for i in range(1, 21):
    if i == num:
        continue
    for j in range(1, 21):
        if j == num or j == i:
            continue
        if (i + j) != 0 and num % (i + j) == 0:
            pairs.append(str(i) + str(j))

result = ' '.join(pairs)

print("Пароль для числа", num, ":", result)
'''

number = int(input("Введите число от 3 до 20: "))


def find_password(num):
    pairs = []
    for i in range(1, num):
        for j in range(i + 1, num + 1):
            if num % (i + j) == 0 and i != j:
                pairs.append((i, j))
    password = ''.join(str(x) + str(y) for x, y in pairs)
    return password


print("Пароль для числа", number, ":", find_password(number))

print("_______________________________________________________________________________")
print('Дополнительное практическое задание по модулю: "Основные операторы": выполнено')
