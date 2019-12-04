#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/18 17:03:49

import json

with open('words_freq.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

pos_frequency = {}

for _pos in range(20):
    pos_frequency[_pos] = {}
    for _word in data.keys():
        if data[_word][_pos]:
            pos_frequency[_pos][_word] = data[_word][_pos]

json_data = json.dumps(pos_frequency, indent=4, ensure_ascii=False)
with open('pos_freq.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)
