# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def negafibonacci(num: int):
    if num == -1:
        return 1
    elif num == -2:
        return -1
    else:
        return negafibonacci(num + 2) - negafibonacci(num + 1)

def fibonacci(num: int):
    if (num <= 1):
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def fibonacci_list(num: int):
    list = []

    for i in range(-num, 0):
        list.append(negafibonacci(i))

    for i in range(0, num+1):
        list.append(fibonacci(i))

    return list


num = int(input('Введите число: '))
print(fibonacci_list(num))