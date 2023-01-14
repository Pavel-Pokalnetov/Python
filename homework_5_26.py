## Задача 26:
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
import random


def expo(a, b):
    '''
    возведение a в степень b через рекурсивный вызов
    '''
    if b == 1: return a
    return a * expo(a, b - 1)


def test(n):
    for _ in range(n):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        print(f"{a}^{b} = {expo(a, b)}")


test(10)
