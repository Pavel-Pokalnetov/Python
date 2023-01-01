'''
## Задача 102: Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# '''

from os import system

def get_simple_number_list(N):
    '''
    возвращает список простых чисел от 2 до N '''
    lst = [2]
    for i in range(3, N+1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return (lst)


def get_number_of_prime_factors(N,visual=False):
    def printV(N,i):
        '''визуализация в виде столбика'''
        if visual:
            if N==i:
                print('{0:7d} |'.format(N))
                return
            print('{0:7d} | {1}'.format(N,i))
    
    result = []
    SIMPLE_NUMBERS = get_simple_number_list(N)
    if N in SIMPLE_NUMBERS: #если число простое, то нет смысла искать его множители
        return [N] 
    while True:
        flag = False
        for i in SIMPLE_NUMBERS:
            if N % i == 0:
                result.append(i)
                printV(N,i)
                N //= i
                flag = True
                break
        if not flag:
            if N != 1:
                result.append(N)
                printV(N,N)
            break
    return result

    return result

system('cls')
number = int(input('введите число: '))
prime_factors_list = get_number_of_prime_factors(number,True)
print('\n{}'.format(prime_factors_list))
