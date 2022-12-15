'''
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.  
Выведите минимальное количество монет, которые нужно перевернуть.  
'''
import random,os

def getCoins(dimension):
    '''
    получаем монетки
    '''
    array = []
    for _ in range(dimension):
        array.append(random.randint(0,1))
    #print(array)
    return array

def checkCoins(coins):
    '''
    проверяем, сколько нужно перевенуть
    '''
    eagle=0
    for item in coins:
        eagle+=item
    return eagle if len(coins)-eagle>eagle else len(coins)-eagle



os.system('cls') #закоментить если не Windows

quantity = int(input('введите число монеток: '))
coins = getCoins(quantity)
print(coins)
print(checkCoins(coins))