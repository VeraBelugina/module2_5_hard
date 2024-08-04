number = int(input('Введите число от 3 до 20: '))


def get_password(n):
    couples = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                couples += f'{i}{j}'
    return couples


num = get_password(number)
print(num)
