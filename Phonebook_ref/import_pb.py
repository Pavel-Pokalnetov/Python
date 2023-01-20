import re


def get_file_content(filename):
    content = ''
    with open(filename, 'r', encoding='utf8') as contentfile:
        for item in contentfile:
            content += item
        return content


def parce_vCard(content):
    ready_parse_data = []
    regexp = 'N:\s([а-яёА-ЯЁ]{,20}\;[а-яёА-ЯЁ]{,20}\;[а-яёА-ЯЁ]{,20})\nFN:[а-яёА-ЯЁ]{,20}\s[а-яёА-ЯЁ]{,20}\s[а-яёА-ЯЁ]{,20}\nTEL;cell:([\+]{0,1}[0-9]{1,11})'
    parsedata = list(re.findall(regexp, content))
    if len(parsedata):
        for fio, tel in parsedata:
            ready_parse_data.append(fio.split(';'), tel)
        return ready_parse_data
    else:
        return None


def parse_JSON(content):
    pass
