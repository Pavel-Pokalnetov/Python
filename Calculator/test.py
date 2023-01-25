from os import system
from polandcalc import calc

def test():
    test_list = ("(-1)+4*6",)
    system('cls')
    for item in test_list:
        result = calc(item)
        print(item, "=", result)
        print()

if __name__=="__main__":
    test()