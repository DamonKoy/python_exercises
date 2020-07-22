"""
1、定义一个函数，接收一个整数列表和一个和值sum，在这个列表中找出和为sum的两个整数，返回这两个整数的下标（注：列表中同一个元素不能使用两遍）
例如：nums = [1, 3, 6, 8] sum = 9 -> [0, 3]
2、定义一个函数，接收两个参数file_path和content，把指定内容写入到指定路径的文件中（如果文件存在，则以追加形式写入）
例如：file_path = 'demo/abc.txt' content = '今天天气好晴朗aa'，在当前路径的demo目录下的abc.txt文件中写入内容：今天天气好晴朗aa
3、熟悉json模块，把字典user_info = {'username': '一级棒','password': '333'}写入文件中，再从文件中读取内容并打印出来。
文件的内容和打印的内容格式如下：
{
    "username": "一级棒",
    "password": "333"
}
"""

# 1、定义一个函数，接收一个整数列表和一个和值sum，在这个列表中找出和为sum的两个整数，返回这两个整数的下标（注：列表中同一个元素不能使用两遍）
# 例如：nums = [1, 3, 6, 8] sum = 9 -> [0, 3]


def find_index(nums: tuple, sum: int):
    index_list = []
    for i in range(0, len(nums)):
        for k in range(0, len(nums)):
            if nums[i] + nums[k] == sum and i != k:
                index_list.append(i)
                index_list.append(k)
                return f"{sum} -> {index_list}"
    else:
        return '没有适合的两个值'

nums = [1, 3, 6, 8]
print(find_index(nums, 9))


"""
2、定义一个函数，接收两个参数file_path和content，把指定内容写入到指定路径的文件中（如果文件存在，则以追加形式写入）
例如：file_path = 'data/abc.txt' content = '今天天气好晴朗aa'，在当前路径的demo目录下的abc.txt文件中写入内容：今天天气好晴朗aa

"""


def write_inpath(file_path, content):
    # a为以追加模式打开
    with open(file_path, 'a') as file:
        file.write(content)


file_path = 'data/abc.txt'
content = '今天天气好晴朗aa'
write_inpath(file_path, content)


"""
3、熟悉json模块，把字典user_info = {'username': '一级棒','password': '333'}写入文件中，再从文件中读取内容并打印出来。
文件的内容和打印的内容格式如下：
{
    "username": "一级棒",
    "password": "333"
}
"""
import json


def write_and_read(info: dict):
    file_path = 'data/info.txt'
    with open(file_path, 'w+') as f:
        # indent=4 为美化换行，ensure_ascii=False 这些字符会原样输出
        f.writelines(json.dumps(info, ensure_ascii=False, indent=4))

    with open(file_path, 'r') as fs:
        fs.readlines()


user_info = {'username': '一级棒', 'password': '333'}
write_and_read(user_info)