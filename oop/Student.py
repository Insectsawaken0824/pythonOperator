# -*- coding:utf-8 -*-

'''
__init__()方法，在创建一个对象时默认被调用，不需要手动调用
__init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中出了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)
__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去
当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
当删除一个对象时，python解释器也会默认调用一个方法，这个方法为__del__()方法
当有1个变量保存了对象的引用时，此对象的引用计数就会加1
当使用del删除变量指向的对象时，如果对象的引用计数不会1，比如3，那么此时只会让这个引用计数减1，即变为2，
当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除
'''

import time
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

    def __str__(self):
         return "类似java的toString"

    def __del__(self):
        print ("%s被干掉了"%self.name)

# xiaoming = Student()
# xiaoming.study()

xiaohong = Student("小红",19)
xiaohong.study()
print xiaohong

xiaoming = Student("小明",19)
xiaoming.study()
print xiaoming

xiaohong2 = xiaohong

del xiaohong
time.sleep(2)
del xiaoming
time.sleep(2)
del xiaohong2
time.sleep(2)
