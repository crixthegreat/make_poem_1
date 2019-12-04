#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/24 9:07:31


import sys
import json

with open('couple_words.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

full_data = []
for _ in range(len(data)):
    full_data.append(''.join(data[_]))

full_data = ''.join(full_data)


pingze = {}
not_judged = {}
# 1.【初始化】
#   1-1. 生成字库
#   1-2. 将字库中所有的字，例如  ”人“ ，将其平仄关系记为：50,50
for _ in data:
    if not(_[0] in pingze.keys()):
        pingze[_[0]] = [50, 50, 0]
        not_judged[_[0]] = 1
    if not(_[1] in pingze.keys()):
        pingze[_[1]] = [50, 50, 0]
        not_judged[_[1]] = 1

print('dict initialised')

# 2.【初始化第一个字】人
pingze['人'][0] = 100

for _ in pingze.keys():
    pingze[_][2] = full_data.count(_)

print('words freq counted')

next_word = 1

while next_word:
    next_word = None
    for _ in pingze.keys():
        # 3.【选出参考字】遍历字库中所有的字，
        # 选出 a 值与 b 值相差最大的一个字，
        # 也就是区分的最好的一个字作为参考字。
        if not_judged[_]:
            if next_word:
                if abs(pingze[_][0] - pingze[_][1]) >= abs(pingze[next_word][0] - pingze[next_word][1]):
                    next_word = _
            else:
                next_word = _
    
    if next_word:
        print(next_word, pingze[next_word][0], pingze[next_word][1])
        next_word_pingze = 0
        if pingze[next_word][0] > pingze[next_word][1]:
            # 平
            next_word_pingze = 0
        elif pingze[next_word][0] == pingze[next_word][1]:
            # 不确定
            next_word_pingze = 2
        else:
            # 仄
            next_word_pingze = 1

        # 4.【计算刷新每一个字的 ab 值】
        # 根据参考字的平仄分类，针对数据样本每一个字对
        #（出现在上下两句的第二个字为一对，出现在上下两句的第四个字也为一对）
        # 例如出现一次（人，我），因为'人'是 a 类的，
        # 则'我'字的 b 值 + 1, a 值 - 1
        for _ in data:
            if next_word in _:
                if next_word == _[0]:
                    change_word = _[1]
                else:
                    change_word = _[0]
                if next_word_pingze == 0:
                    pingze[change_word][0] -= 1
                    pingze[change_word][1] += 1
                elif next_word_pingze == 1:
                    pingze[change_word][0] += 1
                    pingze[change_word][1] -= 1

        # 5. 标记参考字为'已参考'。重复步骤3，直至所有的字都已被参考过            
        not_judged[next_word] = 0


with open('pingze.json', 'w', encoding='utf-8-sig') as f:
    f.write(json.dumps(pingze, indent=4, ensure_ascii=False))
