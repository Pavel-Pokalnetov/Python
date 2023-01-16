'''
Задача 2
Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

def GetSumm(number):
    summ = 0
    while(number>0):
        summ +=number%10
        number //= 10
    return summ


if __name__ == '__main__':
    number = int(input('введите число: '))    
    print (f'{number} -> {GetSumm(number)}')


    
    
    