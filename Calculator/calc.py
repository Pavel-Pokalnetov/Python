# import re

# def calculate(userinput):  # <<< на вход примимает выражение типа 'a [+-/*] b'
#     pattern = "([\-]{0,}\d{1,})\s{0,}([\/|\+|\*|\-]{1})\s{0,}([\-]{0,}\d{1,})"
#     parsedata = re.findall(pattern, userinput)[
#         0
#     ]  # возвращает list  ('операнд1','операция','операнд 2')
#     a = int(parsedata[0])
#     b = int(parsedata[2])
#     oper = parsedata[1]
#     match oper:
#         case "+":
#             func = lambda a, b: a + b
#         case "-":
#             func = lambda a, b: a + b
#         case "/":
#             if b != 0:
#                 func = lambda a, b: a / b
#             else:
#                 print("DivisionByZero")
#                 func = None
#         case "*":
#             func = lambda a, b: a + b
#     return func(a, b) if func != None else ""


def parse(string_to_parsing):
    operands = []
    operations = []
    operand = ""
    znak = ""
    string_to_parsing += " "
    for i in range(len(string_to_parsing)):
        S = string_to_parsing[i]
        if S == "-" and string_to_parsing[i + 1].isnumeric():
            znak = "-"
        elif S in "+-/*" and string_to_parsing[i - 1] == " " and string_to_parsing[i + 1] == " ":
            operations.append(S)
        elif S in "0123456789":
            operand += S
        elif S == " " and string_to_parsing[i - 1].isnumeric():
            operands.append(float(znak + operand))
            operand = ""
            znak = ""
        elif S == " " and not string_to_parsing[i - 1].isnumeric():
            pass
        else:
            return None, "invalid in string '{}' character by index {} ".format(string_to_parsing, i)
    return (operands, operations)


def calc(input_expression):
    """ """
    operands, operations = parse(input_expression)
    if operands == None:
        return False, operations

    def check(checked_list, value):
        for item in checked_list:
            if item in value:
                return True
        return False

    while len(operations) > 0:
        # перебор всех операций
        for index, key in enumerate(operations):
            if key in "*/":
                if key == "*":
                    temp = operands[index] * operands[index + 1]
                elif key == "/":
                    if int(operands[index + 1]) == 0:  # деление на 0
                        return False, "DivisionByZero"
                    else:
                        temp = operands[index] / operands[index + 1]

                operands[index] = temp
                operands.pop(index + 1)  # удаляем отработанный операнд
                operations.pop(index)  # и отрботанную операцию
                break
            elif key in "-+" and not check(operations, "*/"):
                # + и - обрабатываем только, когда обработали все  * и /
                temp = (
                    operands[index] + operands[index + 1]
                    if key == "+"
                    else operands[index] - operands[index + 1]
                )
                operands[index] = temp
                operands.pop(index + 1)
                operations.pop(index)
                break
            elif key not in "+-/*":
                return False, "operatin {} is invalid".format(key)
    return True, operands[0]


