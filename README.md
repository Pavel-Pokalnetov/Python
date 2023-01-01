# Домашнее задание Семинар 1

## Задача 2
Найдите сумму цифр трехзначного числа.  
Пример:  
123 -> 6 (1 + 2 + 3)  
100 -> 1 (1 + 0 + 0)  

Решение: [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_1_2.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_1_2.py)

## Задача 4
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?  
Пример:  
6 -> 1 4 1  
24 -> 4 16 4  
60 -> 10 40 10  

Решение: [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_1_4.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_1_4.py)

## Задача 6
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.  
Пример:  
385916 -> yes  
123456 -> no  

Решение: [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_1_6.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_1_6.py)

## Задача 8
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).  
Пример:  
3 2 4 -> yes  
3 2 1 -> no  

Решение:  
1-й вариант: [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_1_8.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_1_8.py)
2-й вариант:
 [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_1_8_%232.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_1_8_%232.py)

---

# Домашннее задание Семинар 2

## Задача 10
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.  
Выведите минимальное количество монет, которые нужно перевернуть.  

5 -> 1 0 1 1 0  
2  

Решение: [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_2_10.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_2_10.py)

## Задача 12
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.  
Помогите Кате отгадать задуманные Петей числа.  

Решение: 
 - вариант 1 [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_2_12.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_2_12.py)
 - вариант 2 [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_2_12%232.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_2_12%232.py)

## Задача 14
Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.  

Решение: [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_2_14.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_2_14.py)

---

# Домашннее задание Семинар 3

## Задача 16:
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь вводит натуральное число N – количество элементов в массиве.
и число, которое необходимо проверить - X.

5  
1 2 3 4 5  
3  
-> 1

Решение: [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_3_16.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_3_16.py)

## Задача 18:
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь вводит натуральное число N – количество элементов в массиве.
и число, которое необходимо проверить - X.

5  
1 2 0 4 7  
6  
  
-> 7

Решение: [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_3_18.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_3_18.py)

## Задача 20:
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:  

A, E, I, O, U, L, N, S, T, R – 1 очко;  
D, G – 2 очка;  
B, C, M, P – 3 очка;  
F, H, V, W, Y – 4 очка;  
K – 5 очков;  
J, X – 8 очков;  
Q, Z – 10 очков.  

А русские буквы оцениваются так:  
А, В, Е, И, Н, О, Р, С, Т – 1 очко;  
Д, К, Л, М, П, У – 2 очка;  
Б, Г, Ё, Ь, Я – 3 очка;  
Й, Ы – 4 очка;  
Ж, З, Х, Ц, Ч – 5 очков;  
Ш, Э, Ю – 8 очков;  
Ф, Щ, Ъ – 10 очков.  

Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы. Для отправки решений необходимо выполнить вход.

Решение:  
* вариант 1  [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_3_20.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_3_20.py)
* вариант 2  [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_3_20_vol2.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_3_20_vol2.py)

---

# Домашнее задание Семинар 4

## Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого набора.
m - кол-во элементов второго набора.
Значения генерируются случайным образом.

Input: 11 6
(значения сгенерированы случайным образом
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18)

Output: 11 6
6 12

Решение:  
- [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_4_22.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_4_22.py)

## Задача 24:
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

Input: 4
(значения сгенерированы случайным образом
4 2 3 1 )

Output: 9

Решение:  
- [https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_4_24.py](https://github.com/Pavel-Pokalnetov/Python/blob/main/homework_4_24.py)


---

# Домашнее задание Семинар 5* (сдавать только к семинару 5!)

## Задача 26:  
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

## Задача 28:
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

---

# Задачи на повторение по материалам предыдущих семинаров (по желанию)

## Задача 101: Вычислить число π c заданной точностью d

Пример: 
при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001

## Задача 102: Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

## Задача 103: Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

Пример:  k=2 

Возможные варианты многочленов:
2*x*x + 4*x + 5 = 0 
x*x + 5 = 0 
10*x*x = 0

## Задача 104: Даны два файла file1.txt и file2.txt, в каждом из которых находится запись многочлена (полученные в результате работы программы из задачи 103). Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.

## Задача 105: Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

## Задача 106: Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 20*23* конфеты. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)

## Задача 107: Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)


## Задача 108: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (модуль в отдельном файле, импортируется как библиотека)

метод Упаковка: на вход подается текстовый файл, на выходе текстовый файл со сжатием.

метод Распаковка: на вход подается сжатый текстовый файл, на выходе текстовый файл восстановленный.
Прикинуть достигаемую степень сжатия (отношение количества байт сжатого к исходному).