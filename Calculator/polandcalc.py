'''клькулятор с учетом приоритата операций (+-/*:) С ПОДДЕРЖКОЙ СКОБОК'''
import math
from os import system


class InvalidIdentifier(Exception):
    pass


def str2pool(expression_string):
    result = []
    pool = list(expression_string)
    num = znak = ""
    oldtoken = "("
    for token in pool:
        if token == " ":
            continue
        if token == '-':
            if oldtoken in "+-*/(^":
                znak = "-"
            elif oldtoken in "0123456789":
                result.append(znak+num)
                result.append(token)
                num = znak = ""
            elif oldtoken in ")":
                result.append(token)
        elif token in '+/*()^':
            if num != '':
                result.append(znak+num)
                num = znak = ''
            result.append(token)
        elif token.isnumeric() or token == '.':
            num += token
        oldtoken = token
    if num != "":
        result.append(znak+num)
    return result


def priority_of_operations(operation):
    match operation:
        case "+" | "-":
            return 1
        case "/" | "*":
            return 2
        case "^":
            return 3
    return 0


def isNumber(token):
    '''
    проверка строки на принадлежность к 
    отрицательным или положительным вещественным числам
    '''
    ttoken = list(token)
    if len(ttoken) == 0:
        return False
    if (ttoken[0] == '-' and len(ttoken) > 1):
        ttoken.pop(0)
    for item in ttoken:
        if item not in '0123456789.':
            return False
    return True


def infix2polan(pool):
    '''конвертирование инфиксной записи в обратную польскую'''
    #  https://ru.wikipedia.org/wiki/Обратная_польская_запись#Вычисления_на_стеке
    result = []
    stack = []
    while (True):
        if len(pool) == 0:
            break
        pass
        token = pool.pop(0)
        if isNumber(token):
            result.append(float(token))
            continue
        elif token in "-+*/^":
            if len(stack) > 0:
                wt_token = priority_of_operations(token)
                while (wt_token <= priority_of_operations(stack[-1])):
                    result.append(stack.pop())
                    if len(stack) == 0:
                        break
            stack.append(token)
            continue
        elif token == ")":
            while (True):
                if len(stack) == 0:
                    print("error")
                    exit()
                if stack[-1] == '(':
                    stack.pop()
                    break
                result.append(stack.pop())
            continue
        elif token == "(":
            stack.append("(")
        else:
            raise InvalidIdentifier
        pass
    while (len(stack) > 0):
        result.append(stack.pop())
    return result


def polandcalc(pool, fl=False):
    '''стековый калькулятор обратной польской записи'''
    oper = {'+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '^': lambda a, b: a**b, }
    stack = []
    while (len(pool) > 0):
        token = pool.pop(0)
        if type(token) == float:
            stack.append(token)
        elif token in '+-*^':
            b = stack.pop()
            a = stack.pop()
            func = oper[token]
            stack.append(func(a, b))
        elif token == "/":
            b = stack.pop()
            a = stack.pop()
            if b != 0:
                stack.append(a/b)
            else:
                return ("ZeroDivisionError")
        else:
            raise ('Undefined token')

    return (stack.pop())


def calc(user_expression):
    try:
        return polandcalc(infix2polan(str2pool(user_expression)))
    except InvalidIdentifier:
        return 'InvalidIdentifier'
    except ZeroDivisionError:
        return 'ZeroDivisionError'


def test(testexpr='((2+ 3)^ 2+(-1))/2 ^3'):
    system("cls")
    print(testexpr)
    strpool = str2pool(testexpr)
    print("ПС   =  [ {} ] ".format("".join(strpool)))
    polandRecord = infix2polan(strpool)

    print("ОПЗ  =  [ {} ] ".format(polandRecord))
    print('{} = {}'.format(testexpr, polandcalc(polandRecord)))
    print()


if __name__ == '__main__':

    test()
