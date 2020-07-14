"""
1、定义一个函数print_days()，接收2个参数year和month，其中year是年份，month是月份，输出year年month月的天数
2、定义一个函数remove_duplicate_digit_and_letter()，接收一个字符串word，去除掉字符串中重复的数字和字母，非字母和数字的字符即保留，例如 "1211abccd&&e8fe$$g" -> "12abcd&&e8f$$g"
3、定义一个排序函数sort_num()，接收2个参数num_list和reverse，其中num_list是一个数字列表，reverse代表排序规则，默认是从小到大排序，reverse为True是从大到小排序，返回排好序的数字列表（注：不能使用内置的排序函数）
"""


"""
1、定义一个函数print_days()，接收2个参数year和month，其中year是年份，month是月份，输出year年month月的天数
"""


# 不使用内置函数的解法：
def print_das(year, month):
    # 大月为31天，小月为30天，2月特殊：非闰年28天，闰年29天
    big_month = [1, 3, 5, 7, 8, 10, 12]
    if month in big_month:
        result = f"{year}年{month}月的天数有31天"
    elif month == 2:
        # 世纪闰年：能被400整除。普通闰年：能被4整除但不能被100整除。
        if year % 400 == 0 or (year % 100 != 0 and year % 4 ==0):
            result = f"{year}年{month}月的天数有29天"
        else:
            result = f"{year}年{month}月的天数有28天"
    else:
        result = f"{year}年{month}月的天数有30天"
    return result

# 使用内置函数的解法：
#import calendar

# def print_das(year, month):
#     # calendar.monthrange函数输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数
#     monthRange = calendar.monthrange(year, month)
#     month_days = monthRange[-1]
#     print(f"{year}年{month}月的天数有{month_days}")


days = print_das(2013, 13)
print(days)


"""
2、定义一个函数remove_duplicate_digit_and_letter()，接收一个字符串word，去除掉字符串中重复的数字和字母，非字母和数字的字符即保留，例如 "1211abccd&&e8fe$$g" -> "12abcd&&e8f$$g"
"""
b = '1211abccd&&e8fe$$g'


# def remove_duplicate_digit_and_letter(word):
#     content = ''
#     for i in word:
#         if i.isalnum() == False or i not in content:
#                 content = content + i
#     return content
#
#
# b = remove_duplicate_digit_and_letter(a)
# print(b)

def remove_duplicate_digit_and_letter(word: str):
    word_list = []
    for char in word:
        # 判断
        if (char.isalnum() and char not in word) or char.isalnum():
            word_list.append(char)
    return ''.join(word_list)


print(remove_duplicate_digit_and_letter(b))

"""
3、定义一个排序函数sort_num()，接收2个参数num_list和reverse，其中num_list是一个数字列表，reverse代表排序规则，默认是从小到大排序，reverse为True是从大到小排序，返回排好序的数字列表（注：不能使用内置的排序函数）
"""
a_list = [2, 1, 5, 6, 2, 2, 4, 3, 1, 9, 3, 8, 4, 2, 1, 0]


def sort_num(num_list=None, reverse=False):
    sort_list = []
    for i in num_list:
        if len(sort_list) == 0:
            sort_list.append(i)
        else:
            for j in sort_list:
                if i >= j:
                    sort_list.insert(sort_list.index(j), i)
                    break
                elif i <= sort_list[-1]:
                    sort_list.append(i)
                    break
    if reverse:
        return sort_list
    else:
        return sort_list[::-1]


c = sort_num(a_list, False)
print(c)

