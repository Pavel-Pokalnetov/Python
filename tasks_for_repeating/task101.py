'''Задача 101: Вычислить число π c заданной точностью d
Пример: 
при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001
'''
import functools
import time
from os import system
import math

def roundM(N,d):
    '''
    отбрасывает дробную часть числа N, меньшую чем d'''
    N = math.trunc(N/d)*d
    return N

# def timer(func):
#     #декоратор  для измерения времени выполнения функции
#     @functools.wraps(func)
#     def _wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         runtime = time.perf_counter() - start
#         print(f"{func.__name__} took {runtime:.4f} secs")
#         return result
#     return _wrapper

#@timer
def getPi(accuracy):
    '''
    возвращает Пи с точностью до accuracy
    и число итераций
    вычисление по методу рядов Мадхавы-Лейбница(Грегори-Лейбница)
    '''
    pi = 0
    n = 1
    delta = 1
    accuracy/=10
    
    while delta>accuracy:
        delta = 1/(2*n-1)
        pi+= delta if (n%2) else -delta
        n+=1
    pi = roundM(pi*4,accuracy*10)
    return pi, n 

system('cls')
d = float(input('введите точность: '))
Pi,n = getPi(d)

print('Пи={} вычислено за {} итераций.'.format(Pi,n))

print('\nПи={}, (из модуля math с округлением до {})'.format(roundM(math.pi,d),d))