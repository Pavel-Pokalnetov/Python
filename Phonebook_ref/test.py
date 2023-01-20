import re
content=''
with open('vCARD.vcf','r',encoding='utf8') as vcardfile:
    for item in vcardfile:
        content += item

    ready_parse_data=[]
    regexp='N:\s([а-яёА-ЯЁ]{,20}\;[а-яёА-ЯЁ]{,20}\;[а-яёА-ЯЁ]{,20})\nFN:[а-яёА-ЯЁ]{,20}\s[а-яёА-ЯЁ]{,20}\s[а-яёА-ЯЁ]{,20}\nTEL;cell:([\+]{0,1}[0-9]{1,11})'
    parsedata = list(re.findall(regexp,content))
    print(len(parsedata))
    for fio,tel in parsedata:
        ready_parse_data.append(fio.split(';'),tel)
    
    print(ready_parse_data)

