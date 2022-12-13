'''
## Задача 8
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если 
разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).  
Пример:  
3 2 4 -> yes  
3 2 1 -> no  
'''

if __name__ == '__main__':
    n = int(input('n='))
    m = int(input('m='))
    k = int(input('k='))

    print(n, m, k, ' -> ', end='')
    
    if k>=n*m or n*m==1:
        print('no')
        exit()
    
    for i in range(1, n//2+1):
        if (k == m*i or k==(m*n-m*i)):
            print('yes')
            exit()
    for i in range(1, m//2+1):
        if (k == n*i or k==(m*n-n*i)):
            print('yes')
            exit()
    print('no')
