# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

input_data = input("Введите элементы списка из вещественных чисел: ")
original = input_data.replace(" ", "").split(",")

list = []

for element in original:
    list_element = str(float(element)).split(".")
    if list_element[1] != '0':
        list.append(list_element[1])

total_list = []
for index in range(len(list)):
    list[index] = "0." + list[index]

min = float(list[0])
max = float(list[0])

for element in list:
    if float(element) > float(max): max = float(element)
    if float(element) < float(min): min = float(element)

print(f"Разница: {max - min}")