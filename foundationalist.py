# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 16:50
# @Author  : damon
# @Site    : 
# @File    : foundationalist
# @Software: PyCharm



"""
列表生成式
"""

# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
# 注意外面是括号，而不是中括号
L = list(range(1, 11))
print(L)

# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环:
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
L = [x * x for x in range(1, 11)]
print(L)

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

# 还可以使用两层循环，可以生成全排列：
L = [m + n for m in 'ABC' for n in 'XYZ']

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
L = [d for d in os.listdir('.')]    # os.listdir可以列出文件和目录
print(L)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
# 输出key=value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

# 因此，列表生成式也可以使用两个变量来生成list：
list = [k + '=' + v for k, v in d.items()]
# 输出['y=B', 'x=A', 'z=C']
print(list)


# 最后把一个list中所有的字符串变成小写：(非字符串类型没有lower()方法)
L = ['Hello', 'work', 'IBM', 'Apple']
list = [s.lower() for s in L]
print(list)



"""
if ... else
在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
"""


# 可以使用isinstance函数判断变量是否为某这种类型
x = 123
y = '123'
print(isinstance(x, int))
print(isinstance(x, str))
print(isinstance(y, int))
print(isinstance(y, str))


# 练习题
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]  # 需要输入的内容
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')



