#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/20 14:56:51

import json

double_word_fix_freq = {}

with open('double_word_fix_freq.json', 'r', encoding='utf-8-sig') as f:
    double_word_data = json.loads(f.read())

double_word_dict_head = {}
double_word_dict_end = {}

for _ in double_word_data.keys():
    if _[0] in double_word_dict_head.keys():
        double_word_dict_head[_[0]].append(_)
    else:
        double_word_dict_head[_[0]] = []
        double_word_dict_head[_[0]].append(_)

    if _[1] in double_word_dict_end.keys():
        double_word_dict_end[_[1]].append(_)
    else:
        double_word_dict_end[_[1]] = []
        double_word_dict_end[_[1]].append(_)


json_data = json.dumps(double_word_dict_head, indent=4, ensure_ascii=False)
with open('double_word_dict_head.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)

json_data = json.dumps(double_word_dict_end, indent=4, ensure_ascii=False)
with open('double_word_dict_end.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)
