'''
## Задача 16:
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь вводит натуральное число N – количество элементов в массиве.
и число, которое необходимо проверить - X.

5  
1 2 3 4 5  
3  
-> 1
'''
import random


def getList(n, min, max):
    i = []
    for _ in range(n):
        i.append(random.randint(min, max))
    return i


def getCountDigitals(number, inputList):
    result = 0
    for item in inputList:
        result += int(item == number)
    return result


def test(counter):
    for _ in range(counter):
        N = random.randint(10, 20);
        X = random.randint(0, 10)
        myList = getList(N, 0, 10);
        count = getCountDigitals(X, myList)
        print('{}\n{}\n{}\n-> {}'.format(N, myList, X, count))
        print('-' * 20)


N = int(input('Введите размер массива: '))
X = int(input('Число для поиска: '))
myList = getList(N, 0, 10)
count = getCountDigitals(X, myList)
print('{}\n{}\n{}\n-> {}'.format(N, myList, X, count))
input('Enter для запуска тестов')
test(10)
