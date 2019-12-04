#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/24 9:07:31

'''
****** FAILED MODEL *************

try to make a rhyme matrix for every words to generate rhyme lists

'''

import sys
import json

'''
统计诗歌样本的押韵情况，尝试进行聚类分析
'''

'''

with open('poem_content.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

poem_sum = len(data)

rhyme_list = {}

for index, _ in enumerate(data):
    #print((index/poem_sum) * 100)
    # 第 10 个字
    word_2 = _[0][9]
    # 第 20 个字
    word_4 = _[1][9]
    if word_2 in rhyme_list.keys():
        pass
    else:
        rhyme_list[word_2] = {}

    if word_4 in rhyme_list.keys():
        pass
    else:
        rhyme_list[word_4] = {}

    if word_4 in rhyme_list[word_2].keys():
        rhyme_list[word_2][word_4] += 1
    else:
        rhyme_list[word_2][word_4] = 1

    if word_2 in rhyme_list[word_4].keys():
        rhyme_list[word_4][word_2] += 1
    else:
        rhyme_list[word_4][word_2] = 1

for _ in list(rhyme_list.keys()):
    for __ in list(rhyme_list[_].keys()):
        if rhyme_list[_][__]==None or rhyme_list[_][__]==1:
            del rhyme_list[_][__]

    _list = list(rhyme_list[_].keys())
    if not _list:
        del rhyme_list[_]

for _ in rhyme_list.keys():
    rhyme_list[_] = sorted(rhyme_list[_].items(), key=lambda x:x[1], reverse=True)

rhyme = []

for _ in rhyme_list.keys():
    sub_rhyme = set()
    sub_rhyme.add(_)
    for __ in rhyme_list[_][:int(len(rhyme_list[_]) * 2/3) + 1]:
        sub_rhyme.add(__[0])

    rhyme.append(list(sub_rhyme))

for index, _ in enumerate(rhyme):
    for sub_index, __ in enumerate(rhyme[index+1:]):
        if _ and __:
            if set(__).issubset(set(_)):
                #print('removed:', __)
                rhyme[index + sub_index + 1] = None
            elif set(_).issubset(set(__)):
                #print('removed:', _)
                rhyme[index] = None

for index, _ in enumerate(rhyme):
    if _ and len(_) <= 4:
        rhyme[index] = None

rhyme_set = [_ for _ in rhyme if _]


with open('rhyme_set.json', 'w', encoding='utf-8-sig') as f:
    f.write(json.dumps(rhyme_set, indent=4, ensure_ascii=False))



