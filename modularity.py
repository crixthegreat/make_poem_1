#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/11/22 9:58:43

import sys

# 打开上面生成的两个 csv 文件
with open('rhyme_nodes.csv', 'r', encoding='utf-8-sig') as f:
    word_list = f.read().split('\n')
    word_list = word_list[1:]
    word_list = word_list[:-1]

with open('rhyme_graph.csv', 'r', encoding='utf-8-sig') as f:
    rhyme_list = f.read().split('\n')
    rhyme_list = rhyme_list[1:]

# 去除用于 Gephi 软件的不必要的信息
for index, _ in enumerate(rhyme_list):
    _ = _.split(',')
    rhyme_list[index] = _[1:3] + _[-1:]

# 一个字典标记一个节点是否已被分析
in_community = {}
for _ in range(len(word_list)):
    in_community[_] = 0

# 整合模块（组）的子程序
def modularise(node, sub_com, g, judge_dict, key_value):
    sub_com.append(node)
    # 标记已纳入某个韵组
    judge_dict[node] = 1
    for _ in g:
        if str(node) in _:
            if str(node) == _[0]:
                next_node = _[1]
            else:
                next_node = _[0]
            # 此处的 200 就是前面提到的参数，越大，分类越模糊，越小越细
            if in_community[int(next_node)]==0 and float(_[2]) < key_value:
                # 递归实现深度搜索
                modularise(int(next_node), sub_com, g, judge_dict, key_value)

modularity_list = []
# 对所有节点，整合到某个韵组中
for node in range(len(word_list)):
    sub_community = []
    if in_community[node] == 0:
        modularise(node, sub_community, rhyme_list, in_community, 200)
        modularity_list.append(sub_community)
            
            
        

# 输出
for _, sub_mod in enumerate(modularity_list):
    print(_, end=' ')
    for word_num in sub_mod:
        print(word_list[word_num][-1], end=' ')
    print('')

print('\n')
# 对于字数太多的组，我们可以用更严格的要求再分组一次
for _ in modularity_list:
    # 大于120个字的组
    if len(_)>120:
        sub_modularity = []
        in_community = {}
        sub_rhyme_list = []
        for _node in _:
            in_community[_node] = 0
        # 提取一个社区的所有的边
        for _edge in rhyme_list:
            if _edge[0] and int(_edge[0]) in _ and int(_edge[1]) in _:
                sub_rhyme_list.append(_edge)
        # 运算
        for node in _:
            sub_community = []
            if in_community[int(node)] == 0:
                modularise(int(node), sub_community, sub_rhyme_list, in_community, 120)
                sub_modularity.append(sub_community)
        # 输出
        for _, sub_mod in enumerate(sub_modularity):
            print(_, end=' ')
            for word_num in sub_mod:
                print(word_list[word_num][-1], end=' ')
            print('')
