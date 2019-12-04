#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/18 13:44:58

import sys
import json

with open('five.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

word_frequency = {}
words_num = 0

for _ in data:
    poem = _['paragraphs']
    if poem:
        for sentence_num, sentence in enumerate(poem):
            sentence = sentence.replace('。', '')
            sentence = sentence.replace('，', '')
            if len(sentence) != 10:
                continue
            for word_num,word in enumerate(sentence):

                pos = word_num + (sentence_num % 2) * 10
                if word in word_frequency.keys():
                    word_frequency[word][pos] += 1
                else:
                    words_num += 1
                    word_frequency[word] = [0 for i in range(20)]
                    try:
                        word_frequency[word][pos] += 1
                    except:
                        print(sentence)
                        print(pos)
                        sys.exit()

json_data = json.dumps(word_frequency, indent=4, ensure_ascii=False)
with open('words_freq.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)
        
print(words_num)

