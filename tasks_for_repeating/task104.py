'''
Задача 104: Даны два файла file1.txt и file2.txt, в каждом из которых находится запись многочлена
(полученные в результате работы программы из задачи 103). 
Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.
'''
from enum import Enum
import os

class State(Enum):

    pass


def getPolinomK(polinom1):
    result = []
    maxDegree = 0
    pol1 = polinom1.strip(' ')[0:-4].replace(' ', '').split('+')
    # print(pol1)
    kDict = dict()
    for item in pol1:
        degree = 0
        if len(item.split('^')) > 1:
            degree += int(item.split('^')[1])
            if maxDegree < degree:
                maxDegree = degree
        index = 0
        k = ''
        while index < len(item):
            if item[index].isdigit():
                k += item[index]
                index += 1
                continue
            if item[index] == 'x' or item[index] == '*':
                if degree == 0:
                    degree = 1
                break
        if k == '':
            k = '1'
        kDict[degree] = int(k)
    return kDict, maxDegree


def polinimSumm(mPolinom1, mPolinom2):
    kDict1, maxDegre1 = getPolinomK(mPolinom1)
    kDict2, maxDegre2 = getPolinomK(mPolinom2)
    maxDegree = maxDegre1 if maxDegre1 >= maxDegre2 else maxDegre2
    kDict = dict()
    for i in range(0, maxDegree+1):
        kDict[i] = kDict1.get(i, 0)+kDict2.get(i, 0)
    resultPol = []
    while maxDegree > 0:
        kf = kDict.get(maxDegree, 0)
        st = ''
        if kf == 0:
            pass
        elif kf == 1:
            st = 'x' if maxDegree == 1 else f'x^{maxDegree}'
        else:
            st = f'{kf}*x' if maxDegree == 1 else f'{kf}*x^{maxDegree}'
        maxDegree -= 1
        if st != '':
            resultPol.append(st)
    if kDict.get(0, 0) != 0:
        resultPol.append(str(kDict.get(0)))
    return resultPol


os.system('cls')
resultPolinoms = []
with open('task103_file1.txt', 'r') as file1:
    with open('task103_file2.txt', 'r') as file2:

        lines1 = file1.readlines()
        lines2 = file2.readlines()

        if len(lines2) != len(lines1):
            print('Количество строк в файле не равно.')

        count_lines = len(lines1) if len(
            lines1) <= len(lines2) else len(lines2)

        for index in range(count_lines):
            mPolinom1 = lines1[index]
            mPolinom2 = lines2[index]

            resPol = polinimSumm(mPolinom1, mPolinom2)
            resPol = ' + '.join(resPol)+' = 0\n'
            resultPolinoms.append(resPol)

            print(mPolinom1[:-4], '  +  ',
                  mPolinom2[:-4], '  =  ', resPol[:-4])
with open('task104_sum.txt', 'w') as outFile:
    for item in resultPolinoms:
        outFile.write(str(item))
