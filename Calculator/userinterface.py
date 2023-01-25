from polandcalc import calc


def start():
    while (True):
        user_expression = input("Выражение: ")
        if user_expression == '':
            exit()
        print("{} = {}".format(user_expression, calc(user_expression)))
