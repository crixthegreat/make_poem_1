#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/12/3 13:29:41

import json

with open('double_word_with_one_word.json', 'r', encoding='utf-8-sig') as f:
    double_word_data = json.loads(f.read())
    

fix_data = {}

for _ in double_word_data.keys():
    fix_data[_] = sorted(double_word_data[_].items(), key=lambda x:x[1], reverse=True) 

for _ in fix_data.keys():
    _list = fix_data[_]
    out_list = []
    for __ in _list:
        out_list.append(__[0])

    fix_data[_] = out_list

json_data = json.dumps(fix_data, indent=4, ensure_ascii=False)
with open('double_word_with_one_word_fix.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)

