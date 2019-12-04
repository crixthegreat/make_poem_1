#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/18 22:40:32


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

sentence_count = len(poem_sentence)
total_text = ''.join(poem_sentence)
print(poem_sentence[10:20])
print(total_text[:100])
print('total sentence:', sentence_count)

word_2 = []
word_1 = []

def split_word(word):
    num = 0
    num_1 = 0
    word = word[:3]

    word1 = word[:2]
    word2 = word[1:]
    
    num = total_text.count(word1)
    num_1 = total_text.count(word2)

    if num >= num_1:
        return (word[2], word1)
    else:
        return (word[0], word2)

i = 0
for sentence in poem_sentence:
    if i%100==0:
        print( 'now parsing...{:.2f}%'.format(i/sentence_count*100))
    word_2.append(sentence[:2])
    word_3 = sentence[2:5]
    _split = split_word(word_3)
    word_1.append(_split[0])
    word_2.append(_split[1])
    #print(_split[0], _split[1])
    i += 1

word_1 = set(word_1)
word_2 = set(word_2)
            
json_data = json.dumps(list(word_1), indent=4, ensure_ascii=False)
with open('word_1.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)

json_data = json.dumps(list(word_2), indent=4, ensure_ascii=False)
with open('word_2.json', 'w', encoding='utf-8-sig') as f:
    f.write(json_data)
