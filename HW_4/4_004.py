# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import os

deegre_of_num = int(input("Введите степень многочлена: "))

polynomial = ""
while deegre_of_num >= 0:
    coefficient = random.randint(0, 100)
    if coefficient != 0:
        match deegre_of_num:
            case 1: polynomial += (str(coefficient) + "*x" + " + ")
            case 0: polynomial += (str(coefficient) + " = 0")
            case _: polynomial += (str(coefficient) + "*x^" + str(deegre_of_num) + " + ")
    deegre_of_num -= 1

path = os.path.join('folder', 'equation.txt')
with open(path, 'w') as data:
    data.write(polynomial)