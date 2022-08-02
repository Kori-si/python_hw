# Реализуйте алгоритм перемешивания списка.

import random

def list_1(number: int):
    list = []
    for i in range(0, number):
        list.append(i)
    return list

def list_mix(list: list):
    for i in range(0, len(list)):
        mix = random.randint(0, len(list)-1)
        list[i], list[mix] = list[mix], list[i]
    return list

num = int(input('Введите размерность создаваемого списка: '))
element = list_1(num)
print(f'Созданный начальный список:{element}')
mixed_list = list_mix(element)
print(f'Перемешанный список:{mixed_list}')