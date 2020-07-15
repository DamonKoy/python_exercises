"""
1、有一个文件user.txt，里面记录的是用户的触漫号和手机号，把文件中的触漫号转换成用户id（截取触漫号第二位到末尾的字符串，16进制转10进制），并保存到新的文件中。
user.txt文件的内容如下：
42E7496A 13875884676
42E74968 15876483743
42E74967 15768465847
42E74966 14897434534
2、有一个列表[1,20,30,[1,44,[4,37,[15,24,33,[18,[22,12,45,[37,15]]]]]]]，用递归的思想打印出所有的值
3、定义一个函数，判断一个key是否在某个字典中（注：字典有可能是嵌套字典）
"""

with open('data/user.txt') as f:     # 文件的读取操作，执行完以下命令则自动退出
    # lines = [line for line in file(file)]
    # print(lines)
    str_list = f.readlines()
    new_list = []
    for i in str_list:
        location = i.find(' ')     # 查找空格的索引
        location_i = str_list.index(i)
        a = i[0:location]       # 赋值a为触漫号
        s = str(int(i[1:location], 16))    # 十六进制转换成十进制
        new_list.append(i.replace(a, s))    # 用新列表存储替换后的所有内容
    with open('data/new_user.txt', 'w+') as fe:
        fe.writelines(new_list)


"""
2、有一个列表[1,20,30,[1,44,[4,37,[15,24,33,[18,[22,12,45,[37,15]]]]]]]，用递归的思想打印出所有的值
"""


def print_list(num_list: tuple):
    for i in num_list:
        if isinstance(i, list):
            print_list(i)
        else:
            print(i)


list1 = [1, 20, 30, [1, 44, [4, 37, [15, 24, 33, [18, [22, 12, 45, [37, 15]]]]]]]
print_list(list1)



"""
3、定义一个函数，判断一个key是否在某个字典中（注：字典有可能是嵌套字典）
"""


def has_key(dict_data={}, key=None):
    if key in dict_data:
        return True   # 如果key在字典中，则结果为True
    else:
        for i in dict_data.values():
            if isinstance(i, dict):     # 判断是否为字典
                if has_key(i, key):  # 判断递归函数的结果
                    return True
    return False   # 输出结果


dict1 = {'name': 'zhangsan', 'year': 1990, 'age': 30, 'high': '180cm',
         'love': {'name': 'xiaobai', 'sport': 'swim'}, 's': {'sport': 'skip'}}


a = has_key(dict1, 'sport')
print(a)