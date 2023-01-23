from os import system
from calc import calc


test_list = (
    "12 + 3 * -3 / 3",  # 9.0
    "-74 + 45 / 14 + 7 * -2",  # -84.78571..
    "12 / 4 + 3 * 3",  # 12.0
    "-74 + 2 * 100!",  # ошибка в 13 символе
    "8 / 0",  # DivisionByZero
    "2 + 4 * 9 * 0 + 1",  # 1
    "-2 + 6 * 2",
)

system('cls')
for item in test_list:
    _, result = calc(item)
    print(item, "=", result)

input('Enter>>>')
