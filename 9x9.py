# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 11:55
# @Author  : damon
# @Site    : 
# @File    : 9*9
# @Software: PyCharm

# 行数
i = 1
while i <= 9:
    # 列数
    j = 1
    while j <= i:
        print(j, '*', i ,'=', j*i, end=' ')
        # 令列数加1
        j += 1
    # 换行
    print('\n')
    # 令行数加1
    i += 1