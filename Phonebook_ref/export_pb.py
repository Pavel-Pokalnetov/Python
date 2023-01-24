from string import Template
from menu import Menu
import json
from function import PHONEBOOKFILE

def export_phonebook():
    menuExport = Menu([("E", "Экспорт адресной книги в vCARD", export_to_vCard),
                       ("J", "Экспорт адресной книги в JSON",  export_to_JSON),
                       ("H", "Экспорт адресной книги в HTML",  export_to_HTML),
                       ("Q", "Выход", -1)])
    while (True):
        if menuExport.run('>:'):
            return


def export_to_vCard():
    tempale_vCard = Template('BEGIN:VCARD\n'
                             'VERSION:2.1\n'
                             'N: $lastname;$firstname;$patronymic\n'
                             'FN:$firstname $patronymic $lastname\n'
                             'TEL;cell:$phonenumber\n'
                             'END:VCARD\n')
    vCARD = ''
    for lastname, firstname, patronymic, phonenumber in read_data_from_file():
        vCARD += tempale_vCard.substitute(lastname=lastname,
                                          firstname=firstname,
                                          patronymic=patronymic,
                                          phonenumber=phonenumber)
    with open('vCARD.vcf', 'w', encoding='utf8') as vCardFile:
        vCardFile.write(vCARD)
        input("файл vCARD.vcf записан\nEnter>")


def export_to_JSON():
    keys = ['lastname',
            'firsname',
            'patronymic',
            'phonenumber']
    records = dict()
    count = 0
    for rawdata in read_data_from_file():
        record = dict(zip(keys, rawdata))
        records[str(count)] = record
        count += 1
    # print(records)
    records = {'phonebook': records}
    with open("phonebook.json", "w", encoding='utf8') as jsonfile:
        json.dump(records, 
                  jsonfile,
                  ensure_ascii=False)
        input("файл phonebook.json записан\nEnter>")


def export_to_HTML():
    template_HTML = Template('''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <title>Телефонный справочник</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
<ol>
 $body
</ol> 
</body>
</html>''')
    template_row = Template(
        '<li>$lastname $firstname $patronymic, $phonenumber</li>\n')
    body = ''
    for lastname, firstname, patronymic, phonenumber in read_data_from_file():
        body += template_row.substitute(lastname=lastname,
                                        firstname=firstname,
                                        patronymic=patronymic,
                                        phonenumber=phonenumber)
    HTML = template_HTML.substitute(body=body)
    with open('phonebook.html', 'w', encoding='utf8') as HTML_File:
        HTML_File.write(HTML)
    input("файл phonebook.html записан\nEnter>")


def read_data_from_file():
    with open(PHONEBOOKFILE, "r", encoding="utf8") as datafile:
        rawdata = list(item.strip('\n').split(',') for item in datafile)
    return rawdata
