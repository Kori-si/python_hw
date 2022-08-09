# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def multipliers(num: int):
    list = []
    for i in range(2, num):
        count = True

        for j in range(2, i):
            if (i % j == 0):
                count = False

        if count and (num % i == 0):
            list.append(i)

    return list


num = int(input('Введите число: '))
list = multipliers(num)
print(f'Список простых множителей числа {num}:{list}')