# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))
 
bin = ''
 
while number > 0:
    bin = str(number % 2) + bin
    number = number // 2
 
print(bin)