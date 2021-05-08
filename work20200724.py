"""
1、git熟悉
（1）github上注册一个账号，本地生成SSH-KEY，并添加与github账号绑定
（2）github上新建一个项目，把项目拉到本地，新增一个READ.md文件，进行第一次提交，push到远程仓库
（3）本地新建一个dev分支，随意新增文件或内容，进行至少2次提交，并push到远程仓库
（4）把dev分支的内容合并到master分支，并push到远程仓库
2、熟悉python中的异常处理，回顾之前的猜数字小游戏，对用户的输入进行异常处理，输入不合法时给出提示，但不中断游戏过程
3、定义一个函数，调用触漫相关接口，完成一个创建社团的业务场景
4、定义一个函数，接收一个字符串参数，判断字符串中的字符是不是都是唯一的
5、定义一个函数，传入一个参数，判断传入的参数是否是一个合法的ip地址
"""
import random
import logging

# # 创建新项目
# git init XXX
# # 初始化本地仓库
# git clone XXX 
# # 新建分支dev
# git checkout -b dev


# 2、熟悉python中的异常处理，回顾之前的猜数字小游戏，对用户的输入进行异常处理，输入不合法时给出提示，但不中断游戏过程
def get_input():
    try:
        num = int(input(f"你猜的答案偏大，请输入你的答案: （{mix}-{num}之间）\n"))
        if isinstance(int) and 

def guess_num():
    result_num = random.randint(1, 100)
    count = 1
    print(f"答案为{result_num}")
    try:
        num = int(input(f"你猜的答案偏大，请输入你的答案: （{mix}-{num}之间）\n"))
        max = 100
        mix = 1
        while num != result_num:
            count += 1
            if num > result_num and (mix <= num <= max):
                # try:
                    max = num
                    num = int(input(f"你猜的答案偏大，请输入你的答案: （{mix}-{num}之间）\n"))
                # except TypeError as e:
                #     logging.exception(e)
                # finally:
                #     num = int(input(f"请输入正确的整数: （{mix}-{num}之间）\n"))
            elif num < result_num and (mix <= num <= max):
                # try:
                    mix = num
                    num = int(input(f"你猜的答案偏小，请输入你的答案: （{num}-{max}之间）\n"))
                # except TypeError as e:
                #     logging.exception(e)
                # finally:
                #     num = int(input(f"请输入正确的整数: （{mix}-{num}之间）\n"))
    print(f"回答正确，正确答案就是{result_num}，你一共猜了{count}次")


guess_num()
