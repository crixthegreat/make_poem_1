#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/22 15:22:32

import sys
import json
import random

with open('pos_top500.json', 'r', encoding='utf-8-sig') as f:
    pos_500_data = json.loads(f.read())

with open('double_word_dict_head.json', 'r', encoding='utf-8-sig') as f:
    double_word_data = json.loads(f.read())

with open('double_word_dict_end.json', 'r', encoding='utf-8-sig') as f:
    double_word_end_data = json.loads(f.read())

with open('pingze_dict_with_prob.json', 'r', encoding='utf-8-sig') as f:
    pingze_data = json.loads(f.read())

with open('double_word_with_one_word_fix.json', 'r', encoding='utf-8-sig') as f:
    double_with_one_word = json.loads(f.read())

rhyme_list = []
with open('rhyme-fix.csv', 'r', encoding='utf-8-sig') as f:
    line = f.readline()
    while line:
        rhyme = [_ for _ in line.split(',')[1:] 
                if _ and _!='\n' and _ in double_word_end_data.keys() ]
        rhyme_list.append(rhyme)
        line = f.readline()

def make_poem(pos_data, double_data, double_end_data, pingze_data, rhyme=['流', '楼']):
    

    def get_pingze(_list, ping=True):
        random.shuffle(_list)
        for _ in _list:
            if ping:
                if not(_[0] in pingze_data[1].keys()):
                    return _[0]
            else:
                if not(_[0] in pingze_data[0].keys()):
                    return _[0]
    
    def get_double_word(word, end=False, ping=True):
        # 自后字取词，用于配押韵字的词
        if end:
            _list = double_end_data[word][:int(len(double_end_data) / 3) + 1]
            pos = 0
        else:
            _list = double_data[word][:int(len(double_data) / 3) + 1]
            pos = 1

        random.shuffle(_list)
        for _ in _list:
            if ping:
                if not(_[pos] in pingze_data[1].keys()):
                    return _
            else:
                if not(_[pos] in pingze_data[0].keys()):
                    return _

        return _list[0]

    def make_sentence(no, pingze_type, word_type, rhyme=rhyme):
        '''make a sentence of a 5-jue poem
                   no: the number of the sentence (1 - 4) 
        pingze_type 0: 仄仄平平仄
        pingze_type 1: 平平仄仄平
        pingze_type 2: 平平平仄仄
        pingze_type 3: 仄仄仄平平
          word_type 0:$$@$$
          word_type 1:$$$$@
        '''
        sentence = ''

        if pingze_type == 0:
            # pingze_type 0: 仄仄平平仄
            word_2 = get_pingze(pos_data[str((no - 1) * 5 + 1)][:300], False)
            sentence += get_double_word(word_2, end=True)
            if word_type:
                word_3 = get_pingze(pos_data[str((no - 1) * 5 + 2)][:300])
                sentence += get_double_word(word_3, False, True)
                sentence += get_pingze(pos_data[str((no - 1) * 5 + 4)][:300], False)
            else:
                word_3 = get_pingze(pos_data[str((no - 1) * 5 + 2)][:300])
                sentence += word_3
                word_4 = get_pingze(pos_data[str((no - 1) * 5 + 3)][:300])
                sentence += get_double_word(word_4, end=False, ping=False)
        elif pingze_type == 1:
            # pingze_type 1: 平平仄仄平
            word_2 = get_pingze(pos_data[str((no - 1) * 5 + 1)][:300], ping=True)
            sentence += get_double_word(word_2, end=True, ping=True)
            if no == 1:
                word_5 = rhyme[2]
            else:
                word_5 = rhyme[int(no / 2) - 1]
            if word_type:
                word_3 = get_pingze(pos_data[str((no - 1) * 5 + 2)][:300], False)
                sentence += get_double_word(word_3, end=False, ping=False)
                sentence += word_5
            else:
                word_3 = get_pingze(pos_data[str((no - 1) * 5 + 2)][:300], ping=False)
                sentence += word_3
                sentence += get_double_word(word_5, end=True, ping=False)
        if pingze_type == 2:
            # pingze_type 2: 平平平仄仄
            word_2 = get_pingze(pos_data[str((no - 1) * 5 + 1)][:300], True)
            sentence += get_double_word(word_2, end=True, ping=True)
            if word_type:
                word_3 = get_pingze(pos_data[str((no - 1) * 5 + 2)][:300])
                sentence += get_double_word(word_3, False, False)
                sentence += get_pingze(pos_data[str((no - 1) * 5 + 4)][:300], False)
            else:
                word_3 = get_pingze(pos_data[str((no - 1) * 5 + 2)][:300])
                sentence += word_3
                word_4 = get_pingze(pos_data[str((no - 1) * 5 + 3)][:300], False)
                sentence += get_double_word(word_4, end=False, ping=False)
        elif pingze_type == 3:
            # pingze_type 1: 仄仄仄平平
            word_2 = get_pingze(pos_data[str((no - 1) * 5 + 1)][:300], ping=False)
            sentence += get_double_word(word_2, end=True, ping=False)
            if no == 1:
                word_5 = rhyme[2]
            else:
                word_5 = rhyme[int(no / 2) - 1]
            if word_type:
                word_3 = get_pingze(pos_data[str((no - 1) * 5 + 2)][:300], ping=False)
                sentence += get_double_word(word_3, end=False, ping=True)
                sentence += word_5
            else:
                word_3 = get_pingze(pos_data[str((no - 1) * 5 + 2)][:300], ping=False)
                sentence += word_3
                sentence += get_double_word(word_5, end=True, ping=True)

        return sentence
    
    _poem = []

    sentence1_type = random.randrange(0, 2)
    pingze_type = random.randrange(0, 4)

    sentence_structure = [
            [0, 1, 2, 3],
            [3, 1, 2, 3],
            [2, 3, 0, 1],
            [1, 3, 0, 1]]

    for _ in range(0, 4):
        _poem.append(make_sentence(_ + 1, sentence_structure[pingze_type][_], random.randrange(0 ,2), rhyme_word))

    return _poem


#rhyme_word = ['烟', '关']
# 输出
for _ in range(5):
    # 取韵字
    random.shuffle(rhyme_list)
    random.shuffle(rhyme_list[0])
    rhyme_word = rhyme_list[0][:3]
    poem = make_poem(pos_500_data, double_word_data, double_word_end_data, pingze_data, rhyme_word)
    for __ in poem:
        print(__)
    print('')
