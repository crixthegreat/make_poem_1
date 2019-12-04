#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/20 14:06:49


import json
import random

with open('pos_top500.json', 'r', encoding='utf-8-sig') as f:
    pos_500_data = json.loads(f.read())

with open('double_word_dict_head.json', 'r', encoding='utf-8-sig') as f:
    double_word_data = json.loads(f.read())

def make_poem(pos_data, double_data):
    def get_double_word(word):
        _list = double_data[word][:int(len(double_data[word]) / 3) + 1]
        random.shuffle(_list)
        return _list[0]

    def make_sentence(no, _type):
        '''
        no: the sentence number
        type 0:$$@$$
        type 1:$$$$@
        '''
        sentence = ''
        word_1 = pos_data[str((no - 1) * 5)][random.randrange(0,500)][0]
        sentence += get_double_word(word_1)
        word_3 = pos_data[str((no - 1) * 5 + 2)][random.randrange(0,500)][0]
        if _type:
            sentence += get_double_word(word_3)
            sentence += pos_data[str((no - 1) * 5 + 4)][random.randrange(0,500)][0]
        else:
            sentence += word_3
            word_4 = pos_data[str((no - 1) * 5 + 3)][random.randrange(0,500)][0]
            sentence += get_double_word(word_4)

        return sentence
    
    _poem = []

    sentence_type = random.randrange(0, 2)
    # sentence 1-2
    _poem.append(make_sentence(1, sentence_type))
    _poem.append(make_sentence(2, sentence_type))

    sentence_type = random.randrange(0, 2)
    # sentence 3-4
    _poem.append(make_sentence(3, sentence_type))
    _poem.append(make_sentence(4, sentence_type))

    return _poem

for _ in range(5):
    poem = make_poem(pos_500_data, double_word_data)
    for __ in poem:
        print(__)
    print('')
