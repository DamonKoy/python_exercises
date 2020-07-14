# test3
result = 0  # 该值用来判断是否已经找到key，没有找到时为0，找到第一个key后赋值为1，当值为1时，不再进行循环


def key_if_exist(dic_data, key):
    global result
    for i in dic_data.keys():
        if not result:
            if i == key:  # data=key
                print(f'{key}在字典中')
                result = 1
                break  # 相等时结束当前循环，并且将result改为1.这样做的目的是如果现在是在嵌套字段中找到的key，result=1后可以作为外面的大循环是否继续的一个判断
            else:  # data≠key
                if isinstance(dic_data[i], dict):  # 判断value是否为嵌套的字典：是的话进行递归判断
                    key_if_exist(dic_data[i], key)
                else:  # data≠key且不是嵌套的字典
                    if i == last_data:  # 当前数据=原字典中最后一个数据：表示已经判断到了所有数据的最后一个，则输出key不在字典中
                        # 存在的bug，key不在字典中且嵌套字典的最后一个数和最外层字典最后一个数相等时，“不在字典中”会重复输出
                        print(f'{key}不在字典中')
        else:
            break


test_data = {
    'name': 'zhan',
    'age': 24,
    'hobby': {
        'music': 'taylor',
        'movie': 'comic'
    },
    'case': 'hh',
    'movie': 'z'
}
last_data = list(test_data.keys())[-1]
key_if_exist(dic_data=test_data, key='movie')
print(11)
key_if_exist(dic_data=test_data, key='movie2')