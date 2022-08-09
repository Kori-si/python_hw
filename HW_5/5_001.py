# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
import random
from random import randint

def player_1(num1):
    while True:
        num1 = int(input("Игрок 1 - введите число: "))
        if 0 < num1 < 29:
            break
        else:
            print("Вы ввели неверное число")
    return num1

def player_2(num2):
    while True:
        num2 = int(input("Игрок 2 - введите число: "))
        if 0 < num2 < 29:
            break
        else:
            print("Вы ввели неверное число")
    return num2

def bot_1(bot):
   bot = randint(1, 28)
   print(f'Бот вводит {bot}')
   return bot

def start_1(count):
    if count == 0:
        print(f'Игру начинает ИГРОК_1. У нас {candi} конфет')
    elif count == 1:
        print(f'Игру начинает ИГРОК_2. У нас {candi} конфет')

def start_2(count):
    if count == 0:
        print(f'Игру начинает ИГРОК_1. У нас {candi} конфет')
    elif count == 1:
        print(f'Игру начинает Бот. У нас {candi} конфет')

def over_1(count):
    if count == 0:
        print(f'Победил игрок 2')
    if count == 1:
        print(f'Победил игрок 1')

def over_2(count):
    if count == 0:
        print(f'Победил бот')
    if count == 1:
        print(f'Победил игрок 1')

num1 = 0
num2 = 0
bot = 0
candi = 100

game = int(input('Выбирите против кого играть: \n- Игрок против игрока = 0:\n- Играть с ИИ = 1:\nВведите число: '))

#  =======================-Игрок против Игрока-===============================

if game == 0:
    while candi >= 1:
        count = randint(0, 1)
        start_1(count)
        if count == 0:
            num1 = int(player_1(num1))
            candi -= num1
            count += 1
            print(f'Осталось {candi} конфет')
            if candi <= 0:
                break
        else:
            count == 1
            num2 = int(player_2(num2))
            candi -= num2
            count -= 1
            print(f'Осталось {candi} конфет')
            if candi <= 0:
                break
    if candi <= 0:
        over_1(count)

#  =======================-Игрок против Бота (тупого)-===============================

if game == 1:
    while candi >= 1:
        count = randint(0, 1)
        start_2(count)
        if count == 0:
            num1 = int(player_1(num1))
            candi -= num1
            count += 1
            print(f'Осталось {candi} конфет')
            if candi <= 0:
                break
        else:
            count == 1
            bot = int(bot_1(bot))
            candi -= bot
            count -= 1
            print(f'Осталось {candi} конфет')
            if candi <= 0:
                break
    if candi <= 0:
        over_2(count)