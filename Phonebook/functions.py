from os import system


class Menu:  # класс меню
    '''
    класс меню
    elements = список кортежей
        кортеж = ("маркер","описание",метод)
        если метод в кортеже==None то возвращает True
        это нужно для реализации выхода из меню реализованных
        во вложенных методах'''

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
                if rummethod == None:
                    return True
                if user_choice == mark:
                    clrscr()
                    rummethod()
                    input('Enter - продолжить')


    def __len__(self):  # размер меню
        return len(self.elements)
