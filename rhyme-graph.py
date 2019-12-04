#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/21 14:41:01

import sys
import json

'''
统计诗歌样本的押韵情况，尝试进行聚类分析
'''
with open('pos_freq.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())

word_9 = data['9']
word_19 = data['19']

word_9_list = sorted(word_9.items(), key=lambda x:x[1], reverse=True)
word_19_list = sorted(word_19.items(), key=lambda x:x[1], reverse=True)
# 取出第 10 个字和第 20 个字的前 1000 个高频字，用于成诗
word_9_list = [_[0] for _ in word_9_list[:1000]]
word_19_list =[_[0] for _ in word_19_list[:1000]]

word_set_9 = set(word_9_list)
word_set_19 = set(word_19_list)
# 合并去重
word_set = word_set_9 | word_set_19


with open('five.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())
# 以下为图论操作
graph = {}
nodes = set()

# 边的格式是：{“甲,乙”:甲与乙押韵的可能性}
def add_rhyme_edge(a, b, G):
    '''
    添加一条押韵的边
    '''
    if a < b:
        a, b = b, a
    
    _key = a + ',' + b
    if _key in G.keys():
        # 此处的 2 代表出现一次所增加的押韵的可能性权重，这是一个重要的参数
        G[_key] += 2
    else:
        G[_key] = 2


def add_not_rhyme_edge(a, b, G):
    '''
    添加一条不押韵的边
    '''
    if a < b:
        a, b = b, a

    _key = a + ',' + b
    if _key in G.keys():
    # 此处的 -10 代表出现一次所增加的不押韵的可能性权重，这也是一个重要的参数
        G[_key] -= 10
    else:
        G[_key] = -10


for _ in data:
    poem = _['paragraphs']
    if len(poem) <= 1:
        continue
    
    i = 0
    two_sentence = poem[i : i+2]
    # 一次取一小节，两句，一共 4 小句诗
    while len(two_sentence)>1:
        # 不是五言的直接不考察
        if len(two_sentence[0]) == 12 and len(two_sentence[1]) == 12:
            #word_1 = two_sentence[0][4]
            # 第 10 个字
            word_2 = two_sentence[0][10]
            # 第 15 个字
            word_3 = two_sentence[1][4]
            # 第 20 个字
            word_4 = two_sentence[1][10]
            # 仅考察高频字集合中的字
            if word_2 in word_set and word_4 in word_set:
                add_not_rhyme_edge(word_3, word_2, graph)
                add_not_rhyme_edge(word_3, word_4, graph)
                add_rhyme_edge(word_2, word_4, graph)
        i += 2
        two_sentence = poem[i : i+2]

keys = list(graph.keys())
for _ in keys:
    # 如果押韵可能性小于 7 ，就去掉这条边
    # 经过多次实验，押韵的界限设为这个值比较合理
    if graph[_] < 7:
        del graph[_]
    else:
        nodes.add(_[0])
        nodes.add(_[-1])

nodes_data = list(nodes)
# 组合成全字符串用于快速统计出现的次数
graph_key_str = ''.join(list(graph.keys()))

for _node in nodes:
    # 如果出现的字数只有两次，仍然不考察
    if graph_key_str.count(_node) <= 2:
        del_list = []
        for _key in graph.keys():
            if _node in _key:
                del_list.append(_key)

        for _key in del_list:
            #print('deleted ', _key)
            del graph[_key]

nodes_new = set()
keys = list(graph.keys())
for _ in keys:
    nodes_new.add(_[0])
    nodes_new.add(_[-1])

nodes_data = list(nodes_new)
# 写入 csv 文件，用于 Gephi 软件分析
with open('rhyme_nodes.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Id,Label\n')
    for id,_ in enumerate(nodes_data):
        f.write(str(id) + ',' + _ + '\n')
# 没事就排个序，以便我等凡夫肉眼观看
graph_sort = sorted(graph.items(), key=lambda x:x[1], reverse=True)

with open('rhyme_graph.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Id,Source,Target,Type,Weight\n')
    i=0
    for _key, _value in graph_sort:
        f.write(str(i) + ',' + str(nodes_data.index(_key[0])) + ',' 
                + str(nodes_data.index(_key[-1])) + ',' 
                + 'undirected' + ',' + str(3000/_value) + '\n' )
        i += 1


