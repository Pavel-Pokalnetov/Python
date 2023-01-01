'''
Задача 24:
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.

'''

from random import randint
from os import system


def shiftList(myList, k=-1):
    '''
    сдвиг списка
    '''
    if k == 0:
        return
    t = k if k > 0 else -k
    if k > 0:
        myList.reverse()
    for _ in range(t):
        myList.append(myList.pop(0))
    if k > 0:
        myList.reverse()


def getList(n, min, max):
    '''
    генерация списка int чисел
    n - размер списка
    min,max - диапазон значений элементов'''
    return [randint(min, max) for _ in range(n)]


def harvesting(_flowerbeds):
    '''
    сбор урожая
    считаем 1ю 2ю и последнюю грядку 
    и обнуляем их
    '''
    result = _flowerbeds[0]+_flowerbeds[1]+_flowerbeds[-1]
    _flowerbeds[0] = _flowerbeds[1] = _flowerbeds[-1] = 0
    return result


def getMaxPerfSweepMachin(_flowerbeds, startPosition):
    harvestOfBeds = []
    maxHarvest = 0
    shiftList(_flowerbeds, -startPosition+1)
    flowerbedsSize = len(_flowerbeds)
    for _ in range(flowerbedsSize):
        harvestone = harvesting(_flowerbeds)
        shiftList(_flowerbeds)
        harvestOfBeds.append(harvestone)
        # print(_,harvestone,harvestOfBeds)
        if maxHarvest < harvestone:
            maxHarvest = harvestone
    flowerbadNumber = []
    for item, value in enumerate(harvestOfBeds):
        if maxHarvest == value:
            flowerbadNumber.append((item+startPosition) % (flowerbedsSize+1))
    shiftList(harvestOfBeds, startPosition-1)
    return (maxHarvest, flowerbadNumber, harvestOfBeds)


if __name__ == '__main__':
    system('cls')
    flowerbedNumbers = int(input('Укажите число грядок: '))
    cropYield = int(input('Максимальная урожайность грядок (кг/грядки): '))
    flowerbeds = getList(
        flowerbedNumbers if flowerbedNumbers > 2 else 3, 1, cropYield)
    print('Всего у нас {} грядок с урожайностью от {} до {}'.format(
        flowerbedNumbers, 1, cropYield))
    print('грядки -> ', flowerbeds)
    startPosition = int(input('перед какой грядкой поместим машину: '))
    perfSweepMashin = getMaxPerfSweepMachin(flowerbeds, startPosition)
    print('Собранный машиной\nурожай -> ', perfSweepMashin[2])
    print('Максимально машина соберет с 3 грядок '
          '{} кг черники, находясь перед {}-й грядкой'.format(perfSweepMashin[0], perfSweepMashin[1]))
