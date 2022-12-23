'''
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого набора.
m - кол-во элементов второго набора.
Значения генерируются случайным образом.
'''
from random import randint
from os import system

system('cls')


def getList(n, min, max):
    '''
    генерация списка int чисел
    n - размер списка
    min,max - диапазон значений элементов'''
    return [randint(min, max) for _ in range(n)]


if __name__ == '__main__':
    n = int(input('введите число n: '))
    m = int(input('введите число m: '))

    nList = getList(n, 0, 20)
    mList = getList(m, 0, 20)

    system('cls')
    print('ИСХОДНЫЕ ДАННЫЕ')
    print(f' n = {n}')
    print(f' m = {m}')
    print('  список №1 {}'.format(nList))
    print('  список №2 {}'.format(mList))

    nSet = set(nList)
    mSet = set(mList)

    print('\nОбщие элементы')
    commonElenemts = sorted(list(nSet & mSet))
    print(commonElenemts)

'''
Вывод результата в консоли:

ИСХОДНЫЕ ДАННЫЕ
 n = 15
 m = 6
  список №1 [7, 11, 6, 12, 6, 9, 4, 14, 2, 18, 0, 7, 1, 4, 11]
  список №2 [18, 11, 17, 9, 6, 14]

Общие элементы
[6, 9, 11, 14, 18]
'''