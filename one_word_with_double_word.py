#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/12/3 13:29:41

import json

with open('double_word_with_one_word_fix.json', 'r', encoding='utf-8-sig') as f:
    double_word_data = json.loads(f.read())
    

one_word_data = {}

for _ in double_word_data.keys():
    for one_word in double_word_data[_]:
        if one_word in one_word_data.keys():
            pass
        else:
            one_word_data[one_word] = []
        one_word_data[one_word].append(_)

for _ in one_word_data.keys():
    _set = set(one_word_data[_])
    _list = list(_set)
    one_word_data[_] = _list
    
json_data = json.dumps(one_word_data, indent=4, ensure_ascii=False)
with open('one_word_with_double_word.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)

