# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


def random_fill_list(size: int, min_value = 0, max_value = 100):
    new_list = []
    for index in range(size + 1):
        new_list.append(randint(min_value, max_value))
    return new_list

random_list = random_fill_list(10, 0, 10)
print(random_list)

new_list = []

for orig_element in random_list:
    count = 0
    for compare_element in random_list:
        if orig_element == compare_element:
            count += 1
    if count == 1:
        new_list.append(orig_element)

print(new_list)