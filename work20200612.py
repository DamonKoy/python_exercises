# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 20:19
# @Author  : damon
# @Site    : 
# @File    : work0612
# @Software: PyCharm


import math


"""
1、给定n=10，计算1! + 2! + 3! + ... + n!的值
"""
# 解法1：
n = 10
factorial = 1
sum = 0
for i in range(1, n+1):
    factorial = i * factorial
    sum += factorial
print(f"阶乘之和{sum}")

# 解法2：
sum1 = 0
n = 10
for i in range(1, n + 1):
    F = math.factorial(i)
    sum1 += F
print(f"阶乘之和{sum1}")


"""
2、给一个数字字符串13543897565，把每一位对应的数字转换成英文数字（例如：“123” -> "one-two-three"）
"""
str = '13543897565'


def f(a):
    list1 = []
    dict1 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "zero"}
    for i in list(a):
        list1.append(dict1[int(i)])
    print("-".join(list1))


f(str)


str1 = '13543897565'


def fa(x):
    dict2 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
             6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "zero"}
    return dict2[int(x)]


r = map(fa, list(str1))
print('-'.join(r))



"""
3、我的关注列表follow_list = {"status":"ok","data":{"follow_list":[{"user_id":"32804516","nickname":"羽秋璃1111233","is_friend":0,"is_vip":1},{"user_id":"35742446","nickname":"我是你的宝贝哦","is_friend":1,"is_vip":1},{"user_id":"264844","nickname":"大鱼噢大鱼","is_friend":0,"is_vip":1},{"user_id":"34362681","nickname":"薛一十三","is_friend":0,"is_vip":0}]}}
（1）如果用户是vip，对用户说“土豪xxx，我关注了你，给个打赏吧”(xxx是用户昵称)
（2）如果用户不是好友关系但是vip（is_friend=0, is_vip=1），对用户说“土豪xxx，我关注了你，给个好友位吧”
"""
follow_list = {"status":"ok","data":{"follow_list":[
    {"user_id":"32804516","nickname":"羽秋璃1111233","is_friend":0,"is_vip":1},
    {"user_id":"35742446","nickname":"我是你的宝贝哦","is_friend":1,"is_vip":1},
    {"user_id":"264844","nickname":"大鱼噢大鱼","is_friend":0,"is_vip":1},
    {"user_id":"34362681","nickname":"薛一十三","is_friend":0,"is_vip":0}]}}

for x in follow_list['data']['follow_list']:
    if x['is_vip'] == 1:
        print(f"土豪{x['nickname']}，我关注了你，给我打赏吧")

for x in follow_list['data']['follow_list']:
    if x['is_vip'] == 1 and x['is_friend'] == 0:
        print(f"土豪{x['nickname']}，我关注了你，给个好友位吧")
