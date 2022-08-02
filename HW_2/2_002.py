# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def summ(num):
    sum = 0
    for i in num:
        if i != '.' and i != '-' and i != 0:
            sum += int(i)
    return(sum)

print(summ(input('Введите вещественное число: ')))

# n = float(input())
 
# suma = 0
# mult = 1
 
# while n > 0:
#     digit = n % 10
#     suma = suma + digit
#     n = n // 10

# print("Сумма:", suma)

# num = input('Введите число: ')

# print(num)

# symb = '.,-/\@'
# for i in symb:
#     num = num.replace(i, '')
# print(num)
# summa =0
# for i in num:
#     summa += int(i)
# print(summa)