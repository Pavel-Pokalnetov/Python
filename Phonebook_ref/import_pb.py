import os
import re
import json
from function import PHONEBOOKFILE, clear_screen
from menu import Menu


def import_phonebook():
    importExport = Menu([("V", "Импорт адресной книги из vCARD", import_vCARD),
                         ("J", "Импорт адресной книги из JSON", import_JSON),
                         ("Q", "Выход", -1)])
    while (True):
        if importExport.run('>:'):
            return


def input_file_for_import():
    clear_screen()
    filename = input('Имя файла для импорта:')
    if os.path.isfile(filename):
        return (filename)
    else:
        print("Файл не существует")
        input("Enter>")
        return -1


def import_vCARD():
    vCARD_file_name =  input_file_for_import() #"vCARD.vcf"
    if vCARD_file_name == -1:
        return
    with open(vCARD_file_name, 'r', encoding='utf8') as contentfile:
        content = contentfile.read()
        result_parsedata = ''
        # используем регулярные выражения для парсинга
        regexp = 'N:\s([а-яёА-ЯЁ]{,20}\;[а-яёА-ЯЁ]{,20}\;[а-яёА-ЯЁ]{,20})\nFN:[а-яёА-ЯЁ]{,20}\s[а-яёА-ЯЁ]{,20}\s[а-яёА-ЯЁ]{,20}\nTEL;cell:([\+]{0,1}[0-9]{1,11})'
        parsedata = list(re.findall(regexp, content))
        if not len(parsedata):
            return
        else:
            for fio, tel in parsedata:
                temp = fio.split(';')
                temp.append(tel)
                result_parsedata += ','.join(temp)+'\n'
            save_data_to_file(result_parsedata)
            print("импорт завершен")
        input("Enter>")


def import_JSON():
    json_file_name = input_file_for_import() # "phonebook.json"
    if json_file_name == -1:
        return
    result_parsedata = ''
    with open(json_file_name, "r", encoding="utf8") as read_file:
        data = json.load(read_file)['phonebook']
        for item in data:
            line = ",".join([data[item]['lastname'],
                            data[item]['firsname'],
                            data[item]['patronymic'],
                            data[item]['phonenumber']])
            result_parsedata += line+'\n'
        save_data_to_file(result_parsedata)
        print("импорт завершен")
        input("Enter>")


def save_data_to_file(datatxt):
    with open(PHONEBOOKFILE, "w", encoding="utf8") as datafile:
        datafile.write(datatxt)
