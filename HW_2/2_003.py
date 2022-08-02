# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def sequence_list(number):
    list1= []

    for n in range(1, number+1):
        list1.append((1 + 1 / n) ** n)
    return list1

def sum_floats_in_list(list):
    sum = 0

    for i in list:
        sum += i

    return sum

num = int(input('Введите N: '))
list = sequence_list(num)
sum = sum_floats_in_list(list)
print(f'Последовательность для N: \n{list}')
print(f'Сумма элементов последовательности = {sum}')