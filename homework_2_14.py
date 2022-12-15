'''
Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.  
'''
from math import pow


def Degree2(n):
    result = []
    i = 0
    while pow(2, i) <= n:
        result.append(int(pow(2,i)))
        i += 1
    return result


number = int(input('введите число: '))
arrayDegreOff2 = Degree2(number)
print(f'{number} -> {arrayDegreOff2}')
