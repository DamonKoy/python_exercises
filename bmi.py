# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 14:44
# @Author  : damon
# @Site    : 
# @File    : BMI
# @Software: PyCharm


"""
if判断
"""
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
height = 1.68
weight = 61.5
bmi = weight/(height * height)
if bmi > 32:
    print('你的BMI指数为 %.2f，属于严重肥胖' % bmi)
elif bmi > 28:
    print('你的BMI指数为 %.2f，属于肥胖' % bmi)
elif bmi > 25:
    print('你的BMI指数为 %.2f，属于过重' % bmi)
elif bmi > 18.5:
    print('你的BMI指数为 %.2f，属于正常' % bmi)
else:
    print('你的BMI指数为 %.2f，属于过轻' % bmi)