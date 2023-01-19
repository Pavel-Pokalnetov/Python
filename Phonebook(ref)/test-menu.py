from os import system

from functions import Menu

# набор методов запускаемых из меню
def run1():
    print('-- 1 --')
    input("Enter to continue")

def run2():
    print('-- 2 --')
    input("Enter to continue")

def run3():
    print('-- 3 --')
    input("Enter to continue")

def run4():
    print('-- 4 --')
    input("Enter to continue")

# элементы меню
menuitems = [
    ('1', 'команда 1', run1),
    ('2', 'команда 2', run2),
    ('3', 'команда 3', run3),
    ('4', 'команда 4', run4),
    ('Q', 'выход', lambda:exit())]

menu = Menu(menuitems)  # создаем меню
menu.run()  # запускаем меню
