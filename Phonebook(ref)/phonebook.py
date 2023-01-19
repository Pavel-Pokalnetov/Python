import time
from os import system
from sys import platform
import re
import functions

PHONEBOOKFILE = "phonebook.txt"  # имя файла справочника
VERSION = "1.1"

def check_phone_number(number):
    return True if len(re.findall("\+{0,1}\d{11}",number))==1 else False

def clear_screen():
    '''очистка экрана (кроссплатформенная)'''
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        system("clear")  # для Linux & MacOS
    else:
        system("cls")  # для Windows


def search_data():
    '''диалог поиска '''
    while True:
        answer = input("Строка поиска(Еnter - выход) >:")
        if answer == "":
            return
        result = search_in_file(answer)
        for printdata in result:
            output_data_string(printdata)
        print("всего найдено записей: {} \n".format(len(result)))


def search_in_file(request):
    '''поиск с возвратом списка найденых записей'''
    result = []
    with open(PHONEBOOKFILE, "r", encoding="utf8") as datafile:
        for line in datafile:
            result.append(line.strip("\n"))
        result = list(filter(lambda line: request in line, result))
    return result


def output_data_string(printdata):
    '''форматированный вывод строки записи'''
    parse_data = printdata.split(",")
    template = "{0:<30} Тел.: {1:<13}"
    print(template.format(
        parse_data[0] + ' ' + parse_data[1] + ' ' + parse_data[2], parse_data[3]))


def save_data_to_file(data_to_save):
    '''запись строки данных в конец файла'''
    data_to_save = ",".join(data_to_save) + "\n"
    print(f'Добавлена запись: {data_to_save}')
    with open(PHONEBOOKFILE, "a", encoding="utf8") as datafile:
        datafile.write(data_to_save)


def print_data():
    '''вывод записей с возвратом числа записей'''
    count = 0
    with open(PHONEBOOKFILE, "r", encoding="utf8") as datafile:
        for line in datafile:
            count += 1
            print(":{:<3} ".format(count), end='')
            output_data_string(line.strip('\n'))
    return count


def print_all_data():
    '''обертка вывод всех записей'''
    clear_screen()
    count = print_data()
    print(">:Всего {} Записей.".format(count))
    input('Enter - продолжить')


def add_data():
    '''добавление записи'''
    clear_screen()
    while True:
        print('Добавление записи(""-выход)>:')
        last_name = input("Фамилия: ")
        if last_name == "":
            return
        first_name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone_number = input("Номер Телефона: ")
        data_to_save = [last_name, first_name, patronymic, phone_number]
        if "" in data_to_save:
            return
        save_data_to_file(data_to_save)


def del_data():
    '''диалог удаления'''
    menu_del = functions.Menu([("N", "удаление по номеру записи", del_data_by_number),
                               ("S", "удаление по строке поиска", del_data_by_search),
                               ("Q", "выход", -1)])
    while (True):
        if menu_del.run():
            return


def del_data_by_search():
    '''удаление по строке поиска'''
    clear_screen()
    while True:
        answer = input("Строка поиска для удаления(''-выход)>:")
        if answer == "":
            return
        found_records = search_in_file(answer)
        if len(found_records) == 0:
            print("нет записей для удаления")
        else:
            print("найдены записи:")
            for printdata in found_records:
                output_data_string(printdata)
            if input('удаляем [Y-да/..-нет]').upper() == "Y":
                phonedata = ""
                with open(PHONEBOOKFILE, "r", encoding="utf8") as datafile:
                    for line in datafile:
                        if answer in line:
                            continue
                        phonedata += line

                with open(PHONEBOOKFILE, "w", encoding="utf8") as datafile:
                    datafile.write(phonedata)


def del_data_by_number():
    '''удаление по порядковому номеру записи'''
    while True:
        clear_screen()
        print_data()
        answer = input("Номер записи для удаления(Q - выход)>: ")
        if answer.upper() == "Q":
            return
        if not answer.isnumeric():
            continue
        answer = int(answer)
        print(answer)
        phonedata = ""
        count = 0
        with open(PHONEBOOKFILE, "r", encoding="utf8") as datafile:
            for line in datafile:
                count += 1
                if answer == count:
                    continue
                phonedata += line

        with open(PHONEBOOKFILE, "w", encoding="utf8") as datafile:
            datafile.write(phonedata)


def edit_data():
    '''редактирование записи(изменение номера)'''
    while (True):
        count_records = print_data()
        answer = input('Введите номер редактируемой записи\n(Q - выход)>:')
        if answer.upper() == "Q":
            return
        answer = int(answer)
        if not (0 < answer <= count_records):
            print('неверный ввод')
            time.sleep(2)
            continue
        not_editable_records = ''  # записи без изменения
        editable_records = ''      # запись для редактирования
        count = 0
        with open(PHONEBOOKFILE, "r", encoding="utf8") as datafile:
            for line in datafile:
                count += 1
                if answer == count:
                    editable_records = line.strip('\n').split(",")
                    continue
                not_editable_records += line

        print("Запись: " + " ".join(editable_records))
        new_number = input("Новый номер(+7XXXXXXXXXX) >: ")
        if not check_phone_number(new_number):
            print("неправильный формат для номера телефона")
            time.sleep(2)
            continue
        editable_records[3] = new_number
        with open(PHONEBOOKFILE, "w", encoding="utf8") as datafile:
            datafile.write(not_editable_records +
                           ",".join(editable_records) + '\n')


if __name__ == "__main__":
    # основной блок
    menuitems = [
        ("P", "Вывод данных", print_all_data),
        ("A", "Добавление записи", add_data),
        ("S", "Поиск", search_data),
        ("D", "Удаление записи", del_data),
        ("R", "Изменение номера записи", edit_data),
        ("Q", "Выход", lambda: exit())]

    menu = functions.Menu(menuitems)
    clear_screen()
    menu.run('>:')
