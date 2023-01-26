from os import system
from polandcalc import calc
from prettytable import PrettyTable

def test():
    test_list = ("((-5.5))*-6+(-4)/-2",
                 "5*5*(-5-2*2+34)/12",)
    system('cls')
    mytable = PrettyTable()
    mytable.field_names = ["Выражение", "Решение", "eval(выражение)","Проверка"]
    for item in test_list:
        result = calc(item)
        mytable.add_row([str(item),result,eval(item),result==eval(item)])
    print(mytable)


if __name__=="__main__":
    test()

