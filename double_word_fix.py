#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/20 14:23:24


import json

double_word_fix = {}

with open('double_word_freq.json', 'r', encoding='utf-8-sig') as f:
    double_word_data = json.loads(f.read())

for _ in double_word_data.keys():
    if double_word_data[_] > 1:
        double_word_fix[_] = double_word_data[_]

double_word_fix_sort = sorted(double_word_fix.items(), key=lambda x:x[1], reverse=True)


json_data = json.dumps(double_word_fix_sort, indent=4, ensure_ascii=False)
with open('double_word_fix.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)
