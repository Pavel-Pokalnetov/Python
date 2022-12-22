COSTCHARS = {
    1: 'АВЕИНОРСТAEIOULNSTR',
    2: 'ДКЛМПУDG',
    3: 'БГЁЬЯBCMP',
    4: 'ЙЫFHVWY',
    5: 'ЖЗХЦЧK',
    8: 'ШЭЮJX',
    10: 'ФЩЪQZ'
}


def getWordCost(word):
    result = 0
    for letter in word:
        for cost, charSet in COSTCHARS.items():
            result += cost if len(set(letter.upper()) & set(charSet)) else 0
    return result


w = "ноутбук"
print(w, " --> ", getWordCost(w))
w = "StarWars"
print(w, " --> ", getWordCost(w))
w = "MegaВольт"
print(w, " --> ", getWordCost(w))
