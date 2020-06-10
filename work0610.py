# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 11:34
# @Author  : damon
# @Site    : 
# @File    : work0610
# @Software: PyCharm


"""
1、有一个文件列表file_list = ["chuman.png", "wechat.exe", "qq.dmg", "a.pngbcd.png", "mumu.exe", "dingding.jpg", "a.png" ]
（1）从中取出所有png文件，组成新的列表png_list
（2）去掉png_list中包含字母'u'的文件
"""
file_list = ["chuman.png", "wechat.exe", "qq.dmg", "a.pngbcd.png", "mumu.exe", "dingding.jpg", "a.png" ]
png_list = [x for x in file_list if '.png' in x]
print(png_list)
print([x for x in png_list if 'u' not in x])


"""
2、生成一个包含1到100的数字列表num_list = [1, 2, ..., 100]，计算列表中所有偶数的和
"""
num_lsit = [ x for x in range(1, 101)]
print('num_list = {0}'.format(num_lsit))
sum_num = sum([x for x in range(1, 101) if x % 2 == 0])
print('列表中所有偶数的和 = %d ' % sum_num)



"""
3、sum = 1 + 2 + 3 + ... + n，输出当sum第一次大于100时，对应的sum和n的值
"""
i = 0
sum = 0
while sum < 100:
    i = i + 1
    sum = sum + i
    # print(i)
    # print('sum = %d ' % sum)
print('sum = {0} , i = {1}'.format(sum, i))



"""
4、有一个服装店资源字典resource_dict = {"status":"ok","data":{"list":[{"id":"15243","title":"Q版音茵百褶","has_buy":1,"price_type":2},{"id":"14990","title":"Q版粉兔小睡衣","has_buy":0,"price_type":1},{"id":"15046","title":"Q版木烟风","has_buy":0,"price_type":1},{"id":"15037","title":"Q版神森儿","has_buy":0,"price_type":2},{"id":"15025","title":"Q版赤阴阳和服","has_buy":0,"price_type":1},{"id":"14769","title":"鬼狱链服","has_buy":1,"price_type":1},{"id":"14552","title":"Q版藤兰校服-男","has_buy":0,"price_type":2}],"act_id":""}}
（1）打印所有已购买资源的id（has_buy字段的值为1）
（2）打印所有价格类型为金币的资源id（price_type字段的值为2）
"""
resource_dict = {"status":"ok","data":{"list":[{"id":"15243","title":"Q版音茵百褶","has_buy":1,"price_type":2},
                    {"id":"14990","title":"Q版粉兔小睡衣","has_buy":0,"price_type":1},
                    {"id":"15046","title":"Q版木烟风","has_buy":0,"price_type":1},
                    {"id":"15037","title":"Q版神森儿","has_buy":0,"price_type":2},
                    {"id":"15025","title":"Q版赤阴阳和服","has_buy":0,"price_type":1},
                    {"id":"14769","title":"鬼狱链服","has_buy":1,"price_type":1},
                    {"id":"14552","title":"Q版藤兰校服-男","has_buy":0,"price_type":2}],"act_id":""}}

data_list = resource_dict['data']['list']
for i in range (0, len(data_list)):
    if data_list[i]['has_buy'] == 1:
        print('已购买的资源id=%s ' % data_list[i]['id'])

for i in range (0, len(data_list)):
    if data_list[i]['price_type'] == 2:
        print('价格类型为金币的资源id=%s ' % data_list[i]['id'])

