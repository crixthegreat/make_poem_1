#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/24 16:26:17


import sys
import json


with open('pingze.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

# [平声字， 仄声字， 多音字， 不确定]
pingze_dict = [{}, {}, {}, {}]


for _ in data.keys():
    prob = abs(data[_][0] - data[_][1]) / 2 / data[_][2]
    if 0 < prob < 0.15:
        pingze_dict[2][_] = prob
        continue

    if data[_][0] > data[_][1]:
        pingze_dict[0][_] = prob
    elif data[_][0] == data[_][1]:
        pingze_dict[3][_] = prob
    else:
        pingze_dict[1][_] = prob


with open('pingze_dict_with_prob.json', 'w', encoding='utf-8-sig') as f:
    f.write(json.dumps(pingze_dict, indent=4, ensure_ascii=False))
