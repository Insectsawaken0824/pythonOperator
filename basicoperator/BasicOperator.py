# -*- coding:utf-8 -*-
# 执行普通的除法
from __future__ import division
# 第一行指定编码
print "你好"
#变量
num1 = 100
num2 = 10
sum = num1 + num2
print sum
#查看变量类型
type = type(sum)
print type

'''关键字
and as assert break class continue def del
elif else except exec finally for from global
if in import is lambda not or pass
print raise return try while with
'''
import keyword

kwlist = keyword.kwlist
print kwlist

'''常用格式符号
%c 字符
%s 通过str()字符串转换来的格式
%i 有符号十进制整数
%d 有符号的十进制整数
%u 无符号的十进制整数
%o 八进制整数
%x 十六进制整数 小写
%X 十六进制整数 大写
%e 索引符号 小写'e'
%E 索引符号 小写'E'
%f 浮点实数
%g %f和%e的简写
%G %f和%E的简写
'''
# 格式符号
age = 10
print "我今年%d岁"%age #数字

age = 18
name = "xiaohua"
print("我是%s,今年%d岁"%(name,age))

# 换行
print "可以换一行\n换就换吧"

# 获取键盘录入
# s = raw_input("请输入\n") #python 3 后去掉 无法解析计算
# print s
# input1 = input("请输入\n") #python 3 后保留 可以解析计算
# print input1

'''
运算符
'''
print 5/2   # 除法
print 5//2  # 整除
print 5**2  # 幂运算

'''
赋值
'''
a,b=1,2
print a
print b

'''
类型转换
'''
# int(a)
# long(a)
# float(a)
# str(a)
# repr(a)     # 转换为表达式
# complex(a)  # 创建一个复数
# eval(a)     # 执行Python表达式
# tuple(a)    # 将序列转换成元祖
# list(a)     # 将序列转换成列表
# chr(a)      # 将整数转换成字符
# unichr(a)   # 将整数转换成Unicode字符
# ord(a)      # 将字符转换为整数值
# hex(a)      # 转换成十六进制
# oct(a)      # 转换成八进制

# 判断
x = 1
if x < 1:
    print x
elif x == 1:
    print x+2
else:
    print x+1

'''
循环
'''
# while循环
a = 1
while a < 10:
    if a < 5 or a > 5:
        print "不是5"
    else:
        print "是5"
    print a
    a += 1

# 99乘法表
i = 1
while i<=9:
    j=1
    while j<=i:
        # 最后加上逗号可以不换行输出
        print ("%d*%d=%-2d "%(j,i,i*j)),
        j+=1
    print('')
    i += 1

# for循环
for x in "nihao":
    if x == 'a':
        break
    elif x=='i':
        continue
    print x
else:
    print "kong"
