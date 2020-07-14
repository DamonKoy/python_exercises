"""
1、定义一个函数，接收一个字符串，重新输出由字符串中的数字组成的一个最大的数字字符串（例如："15477239" -> "97754321"）
2、定义一个函数，接收一个参数（num` >= 1000）,求100到num之间的水仙花数（水仙花数：如果这个数是m位数，则每个位上的数字的m次幂之和等于它本身）
3、定义一个函数记录学生信息，接收任意参数，但只记录name、age、height、weight、sex、address信息，address不传时，默认为广州市，对记录的信息进行打印。
如：
record_student_info(name='小王', sex='女')
record_student_info(name='小明', sex='男', address='北京市')
record_student_info(name='小陈', favorite='运动', height=170)
{'address': '广州市', 'name': '小王', 'sex': '女'}
{'address': '北京市', 'name': '小明', 'sex': '男'}
{'address': '广州市', 'name': '小陈', 'height': 170}
"""

"""
1、定义一个函数，接收一个字符串，重新输出由字符串中的数字组成的一个最大的数字字符串（例如："15477239" -> "97754321"）
"""


def str_to_sort(text: str):
    # 把所有为数字的元素加到列表
    work_list = []
    for char in text:
        if char.isdigit():
            work_list.append(char)
    return ''.join(sorted(text, reverse=True))


str_to_sort("15477239")



"""
2、定义一个函数，接收一个参数（num >= 1000）,求100到num之间的水仙花数（水仙花数：如果这个数是m位数，则每个位上的数字的m次幂之和等于它本身）
"""


# def narcissistic(num: int):
#     num_list = []
#     if num < 1000:
#         print('请输入大于等于1000的整数')
#     else:
#         for i in range(100, num):
#             m = len(str(i))  # 计算i的位数
#             s = 0
#             for j in range(0, m):
#                 a = int(str(i)[j])
#                 s = s + pow(a, m)
#                 j += 1
#             if i == s:
#                 num_list.append(i)
#     print(num_list)

def narcissistic(num: int):
    num_list = []
    for i in range(100, num+1):
        # 看这个是多少位
        length = len(str(i))
        # 每位数转换为一个列表
        str_list = list(str(i))
        # 使用map函数进行幂运算
        # 了解map()函数，了解lambda函数
        new_list = list(map(lambda x: int(x)**length, str_list))
        # 判断i本身与各位数幂的求和
        if i == sum(new_list):
            num_list.append(i)
    return num_list


narcissistic(10000)


"""
3、定义一个函数记录学生信息，接收任意参数，但只记录name、age、height、weight、sex、address信息，address不传时，默认为广州市，对记录的信息进行打印。
如：
record_student_info(name='小王', sex='女')
record_student_info(name='小明', sex='男', address='北京市')
record_student_info(name='小陈', favorite='运动', height=170)
{'address': '广州市', 'name': '小王', 'sex': '女'}
{'address': '北京市', 'name': '小明', 'sex': '男'}
{'address': '广州市', 'name': '小陈', 'height': 170}
"""

# 在 python 中，*args 和 **kwargs 都代表 1个 或 多个 参数的意思。*args 传入tuple 类型的无名参数，而 **kwargs 传入的参数是 dict 类型。下文举例说明。

def record_student_info(address='广州市', **kwargs):
    word = ['name', 'age', 'height', 'weight', 'sex', 'address']
    info = {'address': address}
    for k in kwargs:
        if k in word:
            info[k] = kwargs[k]
    return info


a = record_student_info(name='小王', sex='女')
b = record_student_info(name='小明', sex='男', address='北京市')
c = record_student_info(name='小陈', favorite='运动', height=170)

print(a, b, c)


