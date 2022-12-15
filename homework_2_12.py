'''
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.  
Помогите Кате отгадать задуманные Петей числа.  
'''
import random
from math import sqrt

def helpKaty(S,P):
    D = S*S-4*P
    resultX=0
    if D<0:
        print('Петя чего-то напутал, такой пары не может быть')
    elif D==0:
        resultX = S/2        
    else:
        resultX = (S + sqrt(D))/2
    resultY = S-resultX
    
    if (int(resultX))==resultX and (int(resultY))==resultY:
        print(f'X={int(resultX)} Y={int(resultY)}')    
    else:
        print('Петя лукавит!\nцифры-то не целые')
        print(f'X={resultX:.1f} Y={resultY:.1f}')



plan = [(9,20),
        (15,56),
        (31,220),
        (28,52)]
for item in plan:
    S,P = item
    print(f'S={S} P={P}',end='\t')
    helpKaty(S,P)


'''
X	Y		S	P
5	4		9	20
7	8		15	56
20	11		31	220
2	26		28	52
7	46		53	322
45	12		57	540
17	29		46	493
2	3		5	6
5	6		11	30
7	8		15	56
10	20		30	200

'''