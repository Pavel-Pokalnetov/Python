from os import system


class Menu:  # класс меню
    def __init__(self, elenemts=[]):
        self.elements = elenemts

    def print(self):
        for (mark, text, _) in self.elements:
            print('{} - {}'.format(mark, text))

    def run(self, prompt='выберите команду: '):
        def clrscr(): return system('cls')
        while (True):
            clrscr()
            self.print()
            user_choice = input(prompt)
            for (mark, _, rummethod) in self.elements:
                if user_choice == mark:
                    clrscr()
                    rummethod()
                    input('Enter - продолжить')
                    break

# набор методов запускаемых из меню
def run1():
    print('-- 1 --')

def run2():
    print('-- 2 --')

def run3():
    print('-- 3 --')

def run4():
    print('-- 4 --')

# элементы меню
menuitems = [
    ('1', 'команда 1', run1),
    ('2', 'команда 2', run2),
    ('3', 'команда 3', run3),
    ('4', 'команда 4', run4),
    ('Q', 'выход', lambda:exit())]

menu = Menu(menuitems)  # создаем меню
menu.run()  # запускаем меню
