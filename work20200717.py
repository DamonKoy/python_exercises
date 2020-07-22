"""
1、有2个字典如下，从中找出价格小于1000，并且颜色不是红色的所有产品名称和颜色的组合
name_price = {"test1":876,"test2":1653,"test3":15,"test4":2876}
name_color = {"test1":"yellow","test2":"blue","test3":"red","test4":"orange"}
2、定义一个People类
（1）包含属性name、age、phone、address属性，为People类提供带有所有成员变量的构造器
（2）提供2个方法：eat(food)、print_user_info()
（3）调用eat(food)方法时，输出“name正在吃food”
（4）调用print_user_info()方法时，输出一个包含当前用户的所有属性信息的字典
3、定义一个Student类，继承自People类
（1）新增属性school、grade、class，其中school默认是“广州市第一中学”，不可修改，grade第一次赋值后也不可以修改，class属性可以修改，但对象不能通过属性赋值的方式直接进行修改
（2）Student类调用print_user_info()方法时，需要新增的属性也打印出来
4、新建一个py文件（和People类、Student类不在同一个文件），在该文件中调用各实例化一个People类和Student类的对象，并调用这些对象可以调用的方法
5、安装第三方库requests，熟悉并发送以下请求
（1）m=Api&c=User&a=token（获取某个用户的install_token）
（2）m=Api&c=User&a=user_profile（通过获得的install_token查询用户信息）
（3）m=Api&c=User&a=user_edit（在用户当前签名的后面加上4个随机数字）
"""


name_price = {"test1": 876, "test2": 1653, "test3": 15, "test4": 2876}
name_color = {"test1": "yellow", "test2": "blue", "test3": "red", "test4": "orange"}


def find_dict(price: dict, color: dict):
    dict_key = {}
    for i, k in name_price.items():
        if k > 1000 and name_color[i] != 'red':
            dict_key[i] = name_color[i]
    print(dict_key)


find_dict(name_price, name_color)


"""
2、定义一个People类
（1）包含属性name、age、phone、address属性，为People类提供带有所有成员变量的构造器
（2）提供2个方法：eat(food)、print_user_info()
（3）调用eat(food)方法时，输出“name正在吃food”
（4）调用print_user_info()方法时，输出一个包含当前用户的所有属性信息的字典
"""


class People:
    def __init__(self, name, age, phone, address):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address

    def eat(self, food):
        return f"{self.name}正在吃{food}"

    def print_user_info(self):
        # 模块对象有一个秘密的只读属性 __dict__，它返回用于实现模块命名空间的字典；
        return self.__dict__


p = People('小胖', 18, '13700000001', '广东省天河区')
print(p.eat('甜筒'))
print(p.print_user_info())


"""
3、定义一个Student类，继承自People类
（1）新增属性school、grade、class，其中school默认是“广州市第一中学”，不可修改，grade第一次赋值后也不可以修改，class属性可以修改，但对象不能通过属性赋值的方式直接进行修改
（2）Student类调用print_user_info()方法时，需要新增的属性也打印出来
"""


class Student(People):
    def __init__(self, name, age, phone, address, grade, clas):
        # super() 函数是用于调用父类(超类)的一个方法。 Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
        super().__init__(name, age, phone, address)
        self.__grade = grade
        self.__class = clas
        self.__shcool = '广州市第一中学'

    # 只能使用方法进行再次赋值
    def set_class(self, clas):
        self.__class = clas

    def return_class(self):
        return self.__class


s = Student('小胖', 18, '13700000001', '广东省天河区', '大二', '一班')
s.set_class('四班')
print(s.print_user_info())
