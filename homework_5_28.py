## Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
import random


def summation(a, b):
    '''
    сложение через рекурсию и инкремент/декремент
    '''
    if b == 0: return a
    return summation(a + 1, b - 1)


def test(n):
    for _ in range(n):
        template = '{} + {} = {} | {}'
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        result = summation(a, b)
        testsum = a + b == result
        print(template.format(a, b, result, testsum))


print(f'a=10, b=7,  a+b={summation(10, 7)}')

print('\nтестировние')
test(10)
