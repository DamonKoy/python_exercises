# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 16:28
# @Author  : damon
# @Site    : 
# @File    : work200615
# @Software: PyCharm

import random


"""
1、word = "1g21gf232123ijh3987dh498fnt49dj47f8"，统计word中各个数字出现的次数
"""

word = '1g21gf232123ijh3987dh498fnt49dj47f8'
li = []
for i in word:
    if i.isdigit() and i not in li:
        li.append(i)
        print(f"{i}出现的次数为{word.count(i)}")


"""
2、num = 567，判断num是不是质数（质数：大于1的自然数中除了能被1和本身整除之外，不能被其他的数整除的数）
"""
num = 567
result = 0
for i in range(2, num):
    if num % i == 0:
        print(f"{num}不是质数，能被{i}整除")
        result = 1
        break
if result == 0:
    print(f"{num}是质数")


"""
3、user_list = {"list":[{"nickname":"茶香谜语","club_info":{"club_id":4,"club_name":"一起玩"}},
{"nickname":"风信子","club_info":{}},{"nickname":"西风","club_info":{}},
{"nickname":"可爱美丽","club_info":{"club_id":8,"club_name":"西风和"}}]}
（1）输出没有加入社团的用户的昵称
（2）对于没有加入社团的用户，随机生成社团信息，要求是club_id在100以内且不能和已存在的club_id重复，club_name和用户的昵称一致，最后打印user_list
"""
user_list = {"list":[{"nickname":"茶香谜语","club_info":{"club_id":4,"club_name":"一起玩"}},
                     {"nickname":"风信子","club_info":{}},
                     {"nickname":"西风","club_info":{}},
                     {"nickname":"可爱美丽","club_info":{"club_id":8,"club_name":"西风和"}}
                     ]}
for i in user_list['list']:
    # 字典判断某个key是否存在
    if 'club_id' not in i['club_info']:
        print(f"没有加入社团的用户昵称'{i['nickname']}'")

club_list = []
random_club_id = random.randint(1, 100)
for i in user_list['list']:
    if 'club_id' in i['club_info']:
        # 将遍历到的club_id加到club_list列表里
        club_list.append(i['club_info']['club_id'])
    else:
        # 如果随机club_id在club_list列表里，则再次随机获取
        while random_club_id in club_list:
            random_club_id = random.randint(1, 100)
        i['club_info']['club_id'] = random_club_id
        i['club_info']['club_name'] = i['nickname']
        club_list.append(i['club_info']['club_id'])
print(user_list)

