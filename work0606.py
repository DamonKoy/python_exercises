# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 14:22
# @Author  : damon
# @Site    : 
# @File    : work0606
# @Software: PyCharm

#
"""
1、把一个字符串转成一个列表，然后再把这个列表转成字符串
"abcdefg" -> ['a', 'b', 'c', 'd', 'e', 'f', 'g'] -> "abcdefg"
"""
# 正确答案
content = "abcdefg"
list_content = list(content)
str_content = ''.join(list_content)
print(list_content)
print(str_content)

#
# # 定义string转list方法
# def string_to_list(content):
#     L = []
#     length = len(content)
#     for i in range(0, length):
#         L.append(content[i])
#     print(L)
#     print(type(L))
#
# # 定义list转string方法
# def list_to_string(list):
#     content = ''
#     content = content.join(list)
#     print(content)
#     print(type(content))
#
#
# string_to_list('abcdefg')
# list_to_string(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
#
#
#
"""
2、有一个列表my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，在这个列表的基础上生成如下列表：
[3, 4, 5, 6, 7, 8]
[1, 4, 7, 10]
[10, 8, 6, 4, 2]
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# []里的第一位为起始下标,第二为为末尾(不取),第三位为取的顺序间隔(负数为倒转，并且第一位从后面下标开始取)
print(my_list[2:7])
print(my_list[::3])
print(my_list[::-2])


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #
# # # 输出[3, 4, 5, 6, 7, 8]
# # print(my_list[2:8])
# # # 输出[1, 4, 7, 10]
# # print(my_list[::3])
# # # 输出[10, 8, 6, 4, 2]
# # a = my_list[1::2]
# # b = a[::-1]     # 数组翻转【::-1】
# # print(a.reverse())   # 为什么不行呢?
# # print(b)



"""
3、有一个字典info = {"name": "xiaoming", "age": 18}，把它变成如下的列表：
[('name', 'xiaoming'), ('age', 18)]
"""
info = {"name": "xiaoming", "age": 18}
print(list(info.items()))

#
# # 定义
# def list_to_object(dict):
#     list = tuple(dict)
#     list_value = tuple(dict.values())
#     alist = []
#     i = len(list)
#     print(i)
#     if i > 0:
#         for i in range(0, i-1):
#             alist[i] = list[i] + list_value[i]
#             i += 1
#         print(alist)
#     else:
#         print("数组不符合格式")
#
#
# list_to_object(info)

# print(tuple(info))  # 把字典转化为元组
# print(tuple(info.values())) # 把字典转化为元组
# print(list(info))   # 把字典转化为列表



"""
list数组的方法使用
"""

classmates = ['hjahaahs', 'sdsga', 'sda', 'dfgdfg']

# 最后一个元素索引为len(classmates)-1，也可以直接用-1做索引获取最后一个元素
print(classmates[len(classmates)-1])
print(classmates[-1])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('next')
# 输出['hjahaahs', 'sdsga', 'sda', 'dfgdfg', 'next']
print(classmates)

# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'money')
# 输出['hjahaahs', 'money', 'sdsga', 'sda', 'dfgdfg', 'next']
print(classmates)

# 要删除list末尾的元素，用pop()方法：
classmates.pop()
# 输出['hjahaahs', 'money', 'sdsga', 'sda', 'dfgdfg']
print(classmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(2)
# 输出['hjahaahs', 'money', 'sda', 'dfgdfg']
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[2] = 'hello'
# 输出['hjahaahs', 'money', 'hello', 'dfgdfg']
print(classmates)

# list里面的元素的数据类型也可以不同，比如：
s = ['python', 'java', ['123', 'php'], 'scheme']
print(len(s))
# 要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：
# p = ['123', 'php']
# s = ['python', 'java', p, 'scheme']
# 要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。
print(s[2][1])

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
L = []
print(len(L))



"""
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改。
它也没有append()，insert()这样的方法。
因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
"""
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 所以，只有1个元素的tuple定义时必须加一个逗号','，来消除歧义：
t = (1,)
print(t)




"""
占位符使用
%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
---------
占位符	替换内容
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
"""
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后2位：
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('小明提升的百分点为%.2f %%' % r)



