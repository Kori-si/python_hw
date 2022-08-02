# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

num1 = int(input("Введите отрицательное число: "))
num2 = int(input("Введите положительное число: "))

list_fact = []

for i in range(num1, num2+1):
    list_fact.append(i)
print(list_fact)

element = input("Введите индексы требуемых элементов (через пробел): ")
elements = element.split(" ")

original_list = list_fact

def mult_element(original_list: list, elements: list):
    mult= 1
    for element in elements:
        mult *= original_list[int(element)]
    return mult

print(f"Произведение элементов на позициях {elements} равно {mult_element(list_fact, elements)}")