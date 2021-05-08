#
# list = [1, 2, 3, 4]
# count = 0
#
# for i in list:
#     for j in list:
#         for k in list:
#             if i != j and j != k and i != k:
#                 print(str(i)+str(j)+str(k))
#                 count = count + 1
# print(count)



# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？


# i = int(input('请输入当月利润(单位:元):'))
# phase1 = 100000
# phase2 = 200000
# phase3 = 400000
# phase4 = 600000
# phase5 = 1000000
#
# if i <= phase1:
#     num = i * 0.1
# elif i <= phase2:
#     num = (i - phase1) * 0.075 + (phase1 * 0.1)
# elif i <= phase3:
#     num = (i - phase2) * 0.05
# elif i <= phase4:
#     num = (i - phase3) * 0.03
# elif i <= phase5:
#     num = (i - phase4) * 0.015
# else:
#     num = (i - phase5) * 0.01
#
# print(f"应发放奖金总数:{float(num)}元")




# import math
#
# profit_list = [0, 100000, 200000, 400000, 600000, 1000000]
# profit_value = [0, 0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
# cash = 0
#
# try:
#     my_profit = int(input('请输入你的利润,单位为元:'))
#     for i in range(1, len(profit_list)):
#         if my_profit > profit_list[i]:
#             cash += (profit_list[i] - profit_list[i-1]) * profit_value[i]
#         else:
#             cash += (my_profit - profit_list[i-1]) * profit_value[i]
#             break
# except ValueError as e:
#     print('请输入大于0的数字')
# finally:
#     print(f'奖金为:{math.floor(cash)}元')



# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#
# import math
#
# i = 9
# s = 0
#
# while(math.pow(i, 2) < (s + 100)):
#     i = i + 1
#     while(math.pow(i, 2) > (s + 100)):
#         s = s + 1
#     if math.pow(i, 2) == (s + 100):
#         k = i
#         while(math.pow(k, 2) < (s + 100 + 168)):
#             k = k + 1
#             if math.pow(k, 2) == (s + 100 + 168):
#                 print(s)
#         s = s + 1
#
#
# for i in range(1, 85):
#     if 168 % i == 0:
#         j = 168 / i;
#         if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)




# 题目：输入某年某月某日，判断这一天是这一年的第几天？
#
# import time
# timeStr = input('请输入某年某月某日(格式如:2021.1.20)')
# date = time.strptime(timeStr, "%Y.%m.%d")
# print(f'这一天为这一年的第{date.tm_yday}天')



# 题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
A = 'SDKJFDsdfsdgds'
B = 'dfkjDFMSDGJsad'
C = sorted(A+B)
print(''.join(C))
