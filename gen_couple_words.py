#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/24 15:14:48


import sys
import json


with open('poem_content.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

word_couple = []

def add_couple(word1, word2, _list):
    if word1> word2:
        word1, word2 = word2, word1
    if word1 != word2:
        _list.append((word1, word2))

for _poem in data:
    add_couple(_poem[0][1], _poem[0][6], word_couple)
    add_couple(_poem[0][3], _poem[0][8], word_couple)
    add_couple(_poem[1][1], _poem[1][6], word_couple)
    add_couple(_poem[1][3], _poem[1][8], word_couple)

with open('couple_words.json', 'w', encoding='utf-8-sig') as f:
    f.write(json.dumps(word_couple, indent=4, ensure_ascii=False))

