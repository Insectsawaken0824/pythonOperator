# -*- coding:utf-8 -*-

# 函数的文档说明
def funDoc(a):
    "函数中的文档"
    print "%d"%(a+1)
funDoc(2)

# 通过参数名指定参数传递
print "--------------"
def funArgs(a,b):
    print "a=%d b=%d"%(a,b)
funArgs(2,1)
funArgs(b=2,a=1)

# 函数返回值与java类似


'''
在函数外边定义的变量叫做全局变量
全局变量能够在所有的函数中进行访问
如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错
如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的，小技巧强龙不压地头蛇

在函数中不使用global声明全局变量时不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变量指向新的数据。
对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量。
对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量。
'''
print "--------------"
a = 10
def modify():
    global a
    print a
    a = 100
    print a
modify()

# 在python中可以返回多个值 本质是返回元祖

# 缺省参数
print "--------------"
# 注意：带有默认值的参数一定要位于参数列表的最后面。
def printinfo( name, age = 35 ):
   print "Name: ", name
   print "Age ", age

printinfo(name="miki" )
printinfo( age=9,name="miki" )

# 不定长参数
print "--------------"
def fun(a, b, *args, **kwargs):
    """可变参数演示示例"""
    print "a =", a
    print "b =", b
    print "args =", args
    print "kwargs: "
    for key, value in kwargs.items():
        print key, "=", value
fun(1, 2, 3, 4, 5, m=6, n=7, p=8)

# 引用传参
'''
Python中函数参数是引用传递（注意不是值传递）。对于不可变类型，因变量不能修改，所以运算不会影响到变量自身；
而对于可变类型来说，函数体中的运算有可能会更改传入的参数变量。(与Java相同)
'''

# 匿名函数
# lambda [arg1 [,arg2,.....argn]]:expression
# Lambda函数能接收任何数量的参数但只能返回一个表达式的值
# 匿名函数不能直接调用print，因为lambda需要一个表达式
print "--------------"
sum = lambda a1, a2: a1 + a2
print sum(1,2)

# 函数作为参数传递
print "--------------"
def fun(a, b, opt):
    print "a =", a
    print "b =", b
    print "result =", opt(a, b)
fun(1, 2, lambda x,y:x+y)

# 字典中根据某一个字段排序
print "--------------"
stus = [
    {"name":"zhangsan", "age":18},
    {"name":"lisi", "age":19},
    {"name":"wangwu", "age":17}
]
stus.sort(key=lambda x : x["name"])
for l in stus:
    print l

# python 函数不支持重载