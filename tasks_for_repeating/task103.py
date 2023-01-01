'''Задача 103: Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

Пример:  k=2 
Возможные варианты многочленов:
2*x*x + 4*x + 5 = 0 
x*x + 5 = 0 
10*x*x = 0

'''
import random
import os


def get_polynomial(k):
    result = []
    ktemp=k
    if k<1:
        raise Exception(f'invalid parametr k={k}, must be greater than 0 ')
    while True:
        k=ktemp
        result=[]
        while k >= 0:
            kf = random.randint(0, 3)
            if k == 0:
                if kf > 0:
                    result.append(str(kf))
                break

            if kf == 0:
                k -= 1
                continue

            operand = '*x'*k
            if kf == 1:
                operand = operand[1:]
                result.append(operand)
            else:
                result.append('{}{}'.format(kf, operand))
            k -= 1
        if 'x' in result: # проверка, что коэффициенты при X^n не равны 0
            # если в многочлене все коэффициенты при X равны нулю, то генерируем заново 
            break   
    print(result)
    return (' + '.join(result)+' = 0\n')

def saveFiles(k,n):
    for index in range(2):
        lines = set()
        while len(lines)<n: #собираем неповторяющиеся многочлены
            lines.add(get_polynomial(k))
        with open(f'task103_file{index}.txt', 'w') as outputFile:
            outputFile.writelines(lines)


os.system('cls')
k = int(input('введите степень многочлена: '))
n = int(input('укажите число примеров для генерации: '))

