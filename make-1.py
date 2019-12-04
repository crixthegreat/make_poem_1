#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/19 12:17:48

import json
import random

with open('word_1.json', 'r', encoding='utf-8-sig') as f:
    single_word_data = json.loads(f.read())

with open('word_2.json', 'r', encoding='utf-8-sig') as f:
    double_word_data = json.loads(f.read())

single_word_data = set(single_word_data)
double_word_data = set(double_word_data)

def make_poem(single_data, double_data):

    def make_sentence(sentence_type):
        '''
        type 0:$$@$$
        type 1:$$$$@
        '''
        sentence = ''
        sentence = double_data.pop()
        if sentence_type:
            sentence += double_data.pop()
            sentence += single_data.pop()
        else:
            sentence += single_data.pop()
            sentence += double_data.pop()

        return sentence

    poem = []

    sentence_type = random.randrange(0, 2)
    #poem.append(sentence_type)
    poem.append(make_sentence(sentence_type))
    poem.append(make_sentence(sentence_type))

    sentence_type = random.randrange(0, 2)
    #poem.append(sentence_type)
    poem.append(make_sentence(sentence_type))
    poem.append(make_sentence(sentence_type))

    return poem

for _ in range(5):
    poem = make_poem(single_word_data, double_word_data)
    for __ in poem:
        print(__)
    print('')
