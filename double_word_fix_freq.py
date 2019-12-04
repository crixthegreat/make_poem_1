#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/20 14:36:35


import json

double_word_fix_freq = {}

with open('double_word_fix.json', 'r', encoding='utf-8-sig') as f:
    double_word_fix_data = json.loads(f.read())

for _ in double_word_fix_data:
    double_word_fix_freq[_[0]] = _[1]


json_data = json.dumps(double_word_fix_freq, indent=4, ensure_ascii=False)
with open('double_word_fix_freq.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)
