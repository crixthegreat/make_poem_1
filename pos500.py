#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/18 19:43:55

import json

pos_top500 = {}

with open('pos_freq.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

for _pos in data.keys():
    _data = data[_pos]
    pos_top500[_pos] = sorted(_data.items(), key=lambda x:x[1], reverse=True)[:500]
    print(_pos)
    for _word in pos_top500[_pos]:
        print(_word[0], end=' ')
    print('')
    

json_data = json.dumps(pos_top500, indent=4, ensure_ascii=False)
with open('pos_top500.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)
