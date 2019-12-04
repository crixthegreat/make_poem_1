#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/17 22:55:38

import os
import json
import sys


def file_analyse(file_name, out):
    with open(file_name, 'r', encoding='utf-8-sig') as f:
        data = json.loads(f.read())
    for _poem in data:
        if _poem['paragraphs']:
            # 对于是否是五言诗处理非常简单粗暴
            # 如果第一句加上逗号和句号一共是 12 个字
            # 那就是五言诗
            if len(_poem['paragraphs'][0])==12:
                out.append(_poem)
    return None


pathname = './poem-data/'
out_list = []

for parent,dirnames,filenames in os.walk(pathname):
    for file_name in filenames:
        #print('now parsing file', file_name)
        file_analyse(pathname + file_name, out_list)
    
json_data = json.dumps(out_list, indent=4, ensure_ascii=False)
with open('five.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)



