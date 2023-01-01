# Задача 106: Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2023 конфеты. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)
import os
import random


def clear():
    os.system('cls')


pull = 200
humanStep = 0
clear()
while pull > 0:
    # игра
    while True:
        print('на столе {} конфет' . format(pull))
        humanStep = int(input('сколько возмете: '))
        if 0 < humanStep < 29:
            break
        input('брать можно от 1 до 28')
    pull -= humanStep

    if pull <= 0:
        print('Вы выиграли')
        exit()

    if pull-29 > 28 or pull==29:
        cpuStep = 28
    elif 0 < pull-29 <= 28:
        cpuStep = pull-29
    else:
        cpuStep = pull

    print('компьютер забрал {} конфет'.format(cpuStep))
    pull -= cpuStep
    if pull <= 0:
        print('и выиграл')
        exit()
