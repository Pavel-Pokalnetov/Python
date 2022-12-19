'''
## Задача 18:
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь вводит натуральное число N – количество элементов в массиве.
и число, которое необходимо проверить - X.

5
1 2 0 4 7
6
  
-> 7
'''
from random import randint

def getList(n, min, max):
    i = []
    for _ in range(n):
        i.append(randint(min, max))
    return i

def findElement(X,inList):
    minIndex = 0
    for i in range(0,len(inList)):
        currentItemDelta = abs(X-inList[i])
        minItem=abs(X-inList[minIndex])
        if currentItemDelta==0:
            return X
        if currentItemDelta<minItem:
            minIndex = i;
    return inList[minIndex]

def test(N,X):
    myList = getList(N,0,50)
    result = findElement(X,myList)
    print('{}\n{}\n{}\n-> {}\n{}'.format(N,myList,X,result,'-'*20))


N = int(input('Введите размер массива: '))
X = int(input('Число для поиска: '))
myList = getList(N, 0, 10)
result = findElement(X,myList)
print('{}\n{}\n{}\n-> {}'.format(N,myList,X,result))

input('press Enter to start test')

#test
pullTest = [
    (10,23),
    (15,11),
    (20,48),
    (25,10)
]
for (N,X) in pullTest:
    test(N,X)

