"""
1、定义一个函数，接收2个参数num_list、num，其中num_list是一个已经排好序的数字列表，函数的作用是把num按照排序规律插入到num_list中并返回num_list，例如[1, 4 , 7, 8, 12], 5 -> [1, 4, 5, 7, 8, 12]（注：不要使用内置的排序方法）
2、定义一个函数custom_replace()，实现的是str.replace()的功能，例如custom_replace('good good study, good or bad', 'good', 'haha')，返回的是‘haha haha study, haha or bad’
3、定义一个函数，接收一个正整数num，把这个正整数num分解质因数。例如：num=110，输出110=2*5*11
"""
num_list = [1, 4, 7, 8, 12]


def insert_list(num_list, num):
    # 判断是从大到小排序
    if num_list[0] >= num_list[-1]:
        for i in range(0, len(num_list)):
            if num >= num_list[i]:
                num_list.insert(i, num)
                break
        # 如果for循环正常结束，else中语句执行。如果是break的，则不执行。
        else:
            num_list.append(num)
    # 如果是从小到大
    else:
        for i in range(0, len(num_list)):
            if num <= num_list[i]:
                num_list.insert(i, num)
                break
        else:
            num_list.append(num)
    return num_list


print(insert_list(num_list, 5))



# 2、定义一个函数custom_replace()，实现的是str.replace()的功能，例如custom_replace('good good study, good or bad', 'good', 'haha')，返回的是‘haha haha study, haha or bad’
def custom_replace(content: str, word: str, change: str):
    content.replace(word, change)
    print(content)


custom_replace('good good study, good or bad', 'good', 'haha')


# 3、定义一个函数，接收一个正整数num，把这个正整数num分解质因数。例如：num=110，输出110=2*5*11
    # 了解质因数
    # 迭代判断是否为合数
    # 收集质因数

num_list = []


def get_num(num: int):
    for i in range(2, num):
        if num % i == 0:
            # 要添加字符串的i，最后才能输出X*X*X
            num_list.append(str(i))
            get_num(num // i)
            break
    # 如果for循环正常结束，else中语句执行。如果是break的，则不执行。
    else:
        # 把最后的质数加入列表里
        num_list.append(str(num))
        print(num_list)
        # 判断num本身是否为质数
        if len(num_list) == 1:
            return f"{num}是质素"
    # 输出答案
    return f"{num}={'*'.join((num_list))}"


print(get_num(1110))