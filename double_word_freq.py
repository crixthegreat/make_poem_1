#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/20 13:31:28

import sys
import json

with open('five.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

poem_sentence = []
for _ in data:
    poem = _['paragraphs']
    if poem:
        for sentence in poem:
            sentence = sentence.replace('。', '')
            sentence = sentence.replace('，', '')
            if len(sentence) != 10:
                continue
            poem_sentence.append(sentence[0:5])
            poem_sentence.append(sentence[5:])


json_data = json.dumps(poem_sentence, indent=4, ensure_ascii=False)
with open('poem_sentence.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)


sentence_count = len(poem_sentence)
total_text = ''.join(poem_sentence)
print('total sentence:', sentence_count)

with open('word_2.json', 'r', encoding='utf-8-sig') as f:
    double_word_data = json.loads(f.read())

double_word_freq = {}
double_word_num = len(double_word_data)

for _, word in enumerate(double_word_data):
    if _%100 ==0:
        print(_/double_word_num *100)
    double_word_freq[word] = total_text.count(word)

json_data = json.dumps(double_word_freq, indent=4, ensure_ascii=False)
with open('double_word_freq.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)
