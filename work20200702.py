"""
1、定义一个函数，找出一个列表中第二大的数字
2、有一个环境配置的txt文件，内容如下所示，定义一个函数，接收env（环境）和key（需要获取项）这2个参数，获取对应环境对应项的内容
demo: {"api_url": "https://api-demo.chumanapp.com", "user_id": 1}
api2: {"api_url": "https://api-api2.chumanapp.com", "user_id": 2}
api: {"api_url": "https://api.chumanapp.com", "user_id": 3}
3、定义一个函数，这个函数的作用是返回某个目录下所有的文件名（包括子目录下的文件）
"""

"""
1、定义一个函数，找出一个列表中第二大的数字
"""


def find_second_max_num(num_list: tuple):
    tmp_list = []
    for i in num_list:
        if isinstance(i, list):     #
            find_second_max_num(i)
            break
        elif isinstance(i, int) and i not in tmp_list:  # 判断是否为数字并不在列表中
            tmp_list.append(i)
    else:
        # 判断是否有大于等于2个不同的数字
        if len(tmp_list) > 1:
            # 进行倒序
            tmp_list.sort(reverse=True)
        else:
            return '没有第二大的数字'
    # 取第二大的数
    return tmp_list[1]


    # tmp_list = []
    # if len(num_list) < 2:
    #     print("该数组至少大于等于2个数")
    # else:
    #
    #     num_list.sort(reverse = True)   # reverse = True 降序排序
    #     max_num = num_list[0]
    #     num_list.remove(max_num)       # 去除最大数值相同的项
    #     print(num_list)
    #     print(len(num_list))
    #     if len(num_list):   # 判断数组里是否仍有值
    #         second_max_num = num_list[1]
    #     else:
    #         print('改数组没有第2大的数字')
    #     print(f"数组中第二大的数为{second_max_num}")


# find_second_max_num([342, 123, 23, 43, 72, 903, 903])
print(find_second_max_num([903, 'test', 903]))


"""
2、有一个环境配置的txt文件，内容如下所示，定义一个函数，接收env（环境）和key（需要获取项）这2个参数，获取对应环境对应项的内容
demo: {"api_url": "https://api-demo.chumanapp.com", "user_id": 1}
api2: {"api_url": "https://api-api2.chumanapp.com", "user_id": 2}
api: {"api_url": "https://api.chumanapp.com", "user_id": 3}
"""
import json


def get_env_key(env, key):
    with open('data/config.txt', encoding='utf-8') as f:
        config_list = []
        for line in f.readlines():
            line = line.strip('\n')        # 去掉换行符
            a = line.split(':', 1)      # 以第1个:符号作为分割，用于下面转换为字典
            config_list.append(a)
    # 将配置文件字典化
    config_dict = dict(config_list)

    if env in config_dict and key in config_dict[env]:
        env_config = json.loads(config_dict[env])       # 导入json库，进行json转换
        return env_config[key]
    else:
        return '不存在该值'


print(get_env_key('demo', 'api_url'))


"""
3、定义一个函数，这个函数的作用是返回某个目录下所有的文件名（包括子目录下的文件）
"""
import os


def get_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print('root_dir', root)     # 当前目录路径
        print('sub_dirs', dirs)     # 当前路径下所有子目录
        print('files', files)       # 当前路径下所有非目录子文件


get_file_name('data/')

