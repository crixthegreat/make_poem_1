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

rhyme_list = []
with open('rhyme.csv', 'r', encoding='utf-8-sig') as f:
    line = f.readline()
    while line:
        rhyme = [_ for _ in line.split(',')[1:] if _ and _!='\n']
        rhyme_list.append(rhyme)
        line = f.readline()

def make_poem(pos_data, double_data, double_end_data, rhyme=['流', '楼']):
    
    def get_double_word(word, end=False):
        # 自后字取词，用于配押韵字的词
        if end:
            _list = double_end_data[word][:int(len(double_end_data) / 4) + 1]
        else:
            _list = double_data[word][:int(len(double_data) / 4) + 1]
        random.shuffle(_list)
        return _list[0]

    
    def make_sentence(no, _type, rhyme=rhyme):
        '''
        no: the sentence number
        type 0:$$@$$
        type 1:$$$$@
        '''
        sentence = ''
        word_1 = pos_data[str((no - 1) * 5)][random.randrange(0,300)][0]
        sentence += get_double_word(word_1)
        word_3 = pos_data[str((no - 1) * 5 + 2)][random.randrange(0,300)][0]
        if _type:
            sentence += get_double_word(word_3)
            if no == 1 or no == 3:
                sentence += pos_data[str((no - 1) * 5 + 4)][random.randrange(0,300)][0]
            else:
                # 末字押韵
                sentence += rhyme[int(no / 2) - 1]
        else:
            sentence += word_3
            if no == 2 or no == 4:
                # 末字押韵，然后向前配词
                word_4 = rhyme[int(no /2) - 1]
                sentence += get_double_word(word_4, end=True)
            else:
                word_4 = pos_data[str((no - 1) * 5 + 3)][random.randrange(0,300)][0]
                sentence += get_double_word(word_4)

        return sentence
    
    _poem = []

    sentence1_type = random.randrange(0, 2)
    sentence3_type = random.randrange(0, 2)
    _poem.append(make_sentence(1, sentence1_type))
    _poem.append(make_sentence(2, sentence1_type, rhyme_word))
    _poem.append(make_sentence(3, sentence3_type))
    _poem.append(make_sentence(4, sentence3_type, rhyme_word))

    return _poem


#rhyme_word = ['烟', '关']
# 输出
for _ in range(5):
    # 取韵字
    random.shuffle(rhyme_list)
    random.shuffle(rhyme_list[0])
    rhyme_word = rhyme_list[0][:2]
    poem = make_poem(pos_500_data, double_word_data, double_word_end_data, rhyme_word)
    for __ in poem:
        print(__)
    print('')
