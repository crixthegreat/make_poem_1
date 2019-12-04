#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/24 9:30:41

import json

with open('five.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

poem = []
_poem = []

for _ in data:
    _poem = _['paragraphs']
    if len(_poem) <= 1:
        continue
    i = 0
    two_sentence = _poem[i : i+2]
    if len(two_sentence[0]) !=12 or len(two_sentence[1]) !=12:
        continue


    # 一次取一小节，两句，一共 4 小句诗
    while len(two_sentence)>1:
        two_sentence[0] = two_sentence[0].replace('，', '')
        two_sentence[0] = two_sentence[0].replace('。', '')
        two_sentence[1] = two_sentence[1].replace('，', '')
        two_sentence[1] = two_sentence[1].replace('。', '')
        # 不是五言的直接不考察
        if len(two_sentence[0]) == 10 and len(two_sentence[1]) == 10:
            poem.append(two_sentence)
        i += 2
        two_sentence = _poem[i : i+2]

with open('poem_content.json', 'w', encoding='utf-8-sig') as f:
    f.write(json.dumps(poem, indent=4, ensure_ascii=False))
