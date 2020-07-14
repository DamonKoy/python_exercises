"""
1、定义一个函数，接收2个参数num_list、num，其中num_list是一个已经排好序的数字列表，函数的作用是把num按照排序规律插入到num_list中并返回num_list，例如[1, 4 , 7, 8, 12], 5 -> [1, 4, 5, 7, 8, 12]（注：不要使用内置的排序方法）
2、定义一个函数custom_replace()，实现的是str.replace()的功能，例如custom_replace('good good study, good or bad', 'good', 'haha')，返回的是‘haha haha study, haha or bad’
3、定义一个函数，接收一个正整数num，把这个正整数num分解质因数。例如：num=110，输出110=2*5*11
"""
num_list = [1, 4, 7, 8, 12]


def insert_list(num_list, num):
    result = False
    if num_list[0] >= num_list[-1]:
        result = True
    if result:
        for i in range(0, len(num_list)):
            if num >= num_list[i]:
                num_list.insert(i, num)
                break
        else:
            num_list.append(num)
    else:
        for i in range(0, len(num_list)):
            if num <= num_list[i]:
                num_list.insert(i, num)
                break
        else:
            num_list.append(num)


insert_list(num_list, 5)