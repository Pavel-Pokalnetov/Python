## Задача 105: Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def clear_word(text,word):
    text = text.split(' ')
    result=[]
    for item in text:
        if not word in item:
            result.append(item)
    return(' '.join(result))


text = 'Напишите программу, удаляющую из абвsбв текста все слова, содержащие абв.'

print(clear_word(text,'абв'))



