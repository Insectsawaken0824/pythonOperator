# -*- coding:utf-8 -*-

'''
__init__()方法，在创建一个对象时默认被调用，不需要手动调用
__init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中出了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)
__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去
'''

class Student:

    # 无参的构造
    # def __init__(self):
    #     self.name = "小明"
    #     self.age = 20

    # 传参的构造

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        print("%s在学习"%self.name)
        print("今年%d岁了"%self.age)

# xiaoming = Student()
# xiaoming.study()

xiaohong = Student("小红",19)
xiaohong.study()