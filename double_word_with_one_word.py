#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/20 13:31:28

import sys
import json
import time

with open('poem_sentence.json', 'r', encoding='utf-8-sig') as f:
    poem_data = json.loads(f.read())

with open('word_2.json', 'r', encoding='utf-8-sig') as f:
    double_word_data = json.loads(f.read())

double_word_with_one_word = {}
three_word_num = len(poem_data)

start_time = time.time()

three_words = []

for _ in poem_data:
    three_words.append(_[-3:])

full_three_words = ''.join(three_words)

for _, short_poem in enumerate(three_words):
    if _%1000 ==0:
        cost_time = time.time() - start_time
        left_time = cost_time / 1000 * (three_word_num - _)
        m, s = divmod(left_time, 60)
        h, m = divmod(m, 60)
        print('{:.2}%'.format(_/three_word_num *100), end = ' ')
        print ("time left: %02d:%02d:%02d" % (h, m, s))
        start_time = time.time()


    if short_poem[:2] in double_word_data:
        word = short_poem[:2]
        single_word = short_poem[-1]

        if not(word in double_word_with_one_word.keys()):
            double_word_with_one_word[word] = {}
        if single_word in double_word_with_one_word[word].keys():
            double_word_with_one_word[word][single_word] += 1
        else:
            double_word_with_one_word[word][single_word] = 1
    if short_poem[1:] in double_word_data:
        word = short_poem[1:]
        single_word = short_poem[0]

        if not(word in double_word_with_one_word.keys()):
            double_word_with_one_word[word] = {}
        if single_word in double_word_with_one_word[word].keys():
            double_word_with_one_word[word][single_word] += 1
        else:
            double_word_with_one_word[word][single_word] = 1


json_data = json.dumps(double_word_with_one_word, indent=4, ensure_ascii=False)
with open('double_word_with_one_word.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)
