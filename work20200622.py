"""
1、有一个数列2/1，3/2，5/3，8/5，13/8，21/13...，求这个数列的前20项之和
2、定义一个函数create_verification_code，接收2个参数length、num，随机生成num个长度为length的数字、字母混合验证码，且生成的验证码不能重复，例如：create_verification_code(3, 4) -> ('a13', 'b7f', '7rr', '84s')
3、编写一个猜数字小游戏，运行的时候随机产生一个答案（1-100之间），效果如下：
请输入你猜测的数字：（1-100之间）
38
你猜的答案偏小，请输入你的答案: （38-100之间）
68
你猜的答案偏大，请输入你的答案: （38-68之间）
53
你猜的答案偏大，请输入你的答案: （38-53之间）
46
回答正确，正确答案就是46，你一共猜了4次
"""

import random
import string

# 1、有一个数列2/1，3/2，5/3，8/5，13/8，21/13...，求这个数列的前20项之和


def sum_spec(length):
    up = 2
    down = 1
    item = up / down
    sum = 0
    if length == 1:
        return item
    else:
        for i in range(1, length+1):
            up, down = up + down, up
            sum += up / down
    return sum

"""
2、定义一个函数create_verification_code，接收2个参数length、num，随机生成num个长度为length的数字、字母混合验证码，且生成的验证码不能重复，例如：create_verification_code(3, 4) -> ('a13', 'b7f', '7rr', '84s')
"""


def create_verification_code(length, num):
    code_list = []
    # 将大小写字母和数字组合成一个列表
    select_word = list(string.ascii_letters)
    select_word.extend(list(string.digits))
    for i in range(1, num+1):
        code = ''.join(random.choices(select_word, k=length))
        code_list.append(code)
    return code_list


print(create_verification_code(4, 3))

"""
3、编写一个猜数字小游戏，运行的时候随机产生一个答案（1-100之间），效果如下：
请输入你猜测的数字：（1-100之间）
38
你猜的答案偏小，请输入你的答案: （38-100之间）
68
你猜的答案偏大，请输入你的答案: （38-68之间）
53
你猜的答案偏大，请输入你的答案: （38-53之间）
46
回答正确，正确答案就是46，你一共猜了4次
"""


def guess_num():
    result_num = random.randint(1, 100)
    count = 1
    print(f"请输入你猜的数字：（1-100之间）")
    print(f"答案为{result_num}")
    num = int(input())
    max = 100
    mix = 1
    while num != result_num:
        count += 1
        if num > result_num:
            max = num
            num = int(input(f"你猜的答案偏大，请输入你的答案: （{mix}-{num}之间）\n"))
        elif num < result_num:
            mix = num
            num = int(input(f"你猜的答案偏小，请输入你的答案: （{num}-{max}之间）\n"))
    print(f"回答正确，正确答案就是{result_num}，你一共猜了{count}次")


guess_num()
