# -*- coding:utf-8 -*-
'''
虽然子类没有定义__init__方法，但是父类有，所以在子类继承父类的时候这个方法就被继承了，所以只要创建Bosi的对象，就默认执行了那个继承过来的__init__方法
子类在继承的时候，在定义类时，小括号()中为父类的名字
父类的属性、方法，会被继承给子类
私有的属性，不能通过对象直接访问，但是可以通过方法访问
私有的方法，不能通过对象直接访问
私有的属性、方法，不会被子类继承，也不能被访问
一般情况下，私有的属性、方法都是不对外公布的，往往用来做内部的事情，起到安全的作用
'''
class Animal(object):

    def __init__(self, name='动物', color='白色'):
        self.__name = name
        self.color = color

    def __test(self):
        print(self.__name)
        print(self.color)

    def test(self):
        print(self.__name)
        print(self.color)



class Dog(Animal):
    def dogTest1(self):
        #print(self.__name) #不能访问到父类的私有属性
        print(self.color)


    def dogTest2(self):
        #self.__test() #不能访问父类中的私有方法
        self.test()


A = Animal()
#print(A.__name) #程序出现异常，不能访问私有属性
print(A.color)
#A.__test() #程序出现异常，不能访问私有方法
A.test()

print("------分割线-----")

D = Dog(name = "小花狗", color = "黄色")
D.dogTest1()
D.dogTest2()