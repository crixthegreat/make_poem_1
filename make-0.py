#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/18 20:12:31


import json
import random

with open('pos_top100.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

for _ in range(5):
    poem = []
    for _pos in data.keys():
        _list = data[_pos]
        poem.append(_list[random.randrange(0,100)][0])
    for _, word in enumerate(poem):
        if _ % 5 == 0:
            print('')
        print(word, end='')
        
    print('')
