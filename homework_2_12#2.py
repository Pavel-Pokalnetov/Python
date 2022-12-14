'''
вариант 2
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.  
Помогите Кате отгадать задуманные Петей числа.  
'''
import random
import os


def helpKaty(S, P):
    resultX = resultY = -1
    if S>1000:
	    minRange = S-1000
	    maxRange = 1000
    else:
	    minRange = 0
	    maxRange = S//2+1
    for x in range(minRange,maxRange):
        if (x*x-S*x+P) == 0:
            resultX = x
            resultY = (int)(S-x)
            break
    if resultX == -1:
        print(' Петя чего-то напутал, такой пары не может быть')
    else:
        print(f'{resultX:3} {resultY:6}')


os.system('cls')  # закоментить если не Windows
plan = [(4, 4),
        (5, 6),
        (9, 20),
        (980,1956),
        (950, 45000 ),
        (1000, 999),
        (1100, 100000),
        (900,0)
        ]
print('   S      P       X      Y')
print('---- ------     ---    ---')
for item in plan:
    S, P = item
    print(f'{S:4} {P:6}  -> ', end='')
    helpKaty(S, P)


'''
X	Y		S	P
5	4		9	20
7	8		15	56
20	11		31	220
2	26		28	52

'''
