# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 14:44
# @Author  : damon
# @Site    : 
# @File    : work0608
# @Software: PyCharm

"""
1、对字符串"Welcome To The Python World"进行如下操作：
（1）输出"welcome to the python world"
（2）输出 ['welcome', 'to', 'the', 'python', 'world']
（3）在（1）的基础上，把字符串中的o全部替换成a
（4）在（1）的基础上，把字符串中的第一个o替换成a
（5）在（1）的基础上，把字符串中的空格全部去掉，变成"welcometothepythonworld"
"""
s = 'Welcome To The Python World'
# 将字符串全部改成小写
s1 = s.lower()
print(s.lower())
# 将字符串进行小写并以空格切片。split() 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。str.split(str="", num=string.count(str))
print(s.lower().split())
# 将字符串某个值替换成另一个值
print(s1.replace('o', 'a'))
print(s1.replace('o', 'a', 1))
print(s1.replace(' ', ''))


"""
2、对列表num_list = [1, 5, 8, 1, 3, 12]进行如下操作：
（1）在num_list后面追加一个数字100（变成[1, 5, 8, 1, 3, 12, 100]）
（2）在（1）的基础上，在后面追加一个列表[1, 2, 3, 4, 5]（变成[1, 5, 8, 1, 3, 12, 100, 1, 2, 3, 4, 5]）
（3）在（2）的基础上，对列表进行反向排序（变成[100, 12, 8, 5, 5, 4, 3, 3, 2, 1, 1, 1]）
（4）在（3）的基础上，把数字4从列表中去除（变成[100, 12, 8, 5, 5, 3, 3, 2, 1, 1, 1]）
"""
num_list = [1, 5, 8, 1, 3, 12]
num_list.append(int(100))
# 复制数组
list1 = num_list[:]
print(list1)
# 在数组内添加列表内容
list1.extend([x for x in range(1, 6)])
print(list1)
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
list1.sort(reverse=True)
print(list1)
# 移除数组中的某个值
list1.remove(4)
print(list1)


"""
3、有一个字典info = {'name': 'xiaoli', 'age': 18, 'height': 170}，进行如下操作：
（1）输出info中所有的key（即['name', 'age', 'height']）
（2）输出info中所有的value（即['xiaoli', 18, 170]）
（3）输出info中所有的key-value对（即[('name', 'xiaoli'), ('age', 18), ('height', 170)]）
（4）把age这一项从info中去掉（即 {'name': 'xiaoli', 'height': 170}）

"""
info = {'name': 'xiaoli', 'age': 18, 'height': 170}
# 输出字典中的所有key
print(list(info.keys()))
# 输出字典中所有value
print(list(info.values()))
# 输出字典中所有key-value
print(list(info.items()))
# 移除字典中的某个值
info.pop('age')
print(list(info.items()))

