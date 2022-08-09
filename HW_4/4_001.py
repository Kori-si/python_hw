#Вычислить число c заданной точностью d
#Пример:
#- при d = 0.001, π = 3.141.$    10^{-1} ≤ d ≤10^{-10}
import math

number = input("Введите число")
number = str(number).split('.')

pi = math.pi

print(round(pi, len(number[1])))