from work20200717 import People, Student


# 获取People的所有方法名
P = People('小权', 18, 15600000001, '广东省')
print(P.eat('水果'))
print(P.print_user_info())

S = Student('小权', 18, 15600000001, '广东省', '大二', '一班')
S.eat('哈密瓜')
S.set_class('三班')
print(S.return_class())
print(S.print_user_info())