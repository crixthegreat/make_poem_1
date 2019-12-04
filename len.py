#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/18 13:44:58

import json

with open('five.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

print(len(data))
