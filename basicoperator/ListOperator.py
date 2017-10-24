# -*- coding:utf-8 -*-

# python的列表可以存不同类型的数据
list = ["a", 1, False]
print list[0]
print list[1]
print list[2]

'''
遍历
'''
# for
for l in list:
    print l

# while
i = 0
while i < len(list):
    print list[i]
    i += 1

# 带下标索引遍历
for i,l in enumerate(list):
     print i,l

# 定义一个遍历打印的方法
def foreachPrint(list):
    for l in list:
        print l

'''
添加操作
'''
# append 向列表追加元素 如果也是列表,则会把列表当做一个元素,加入到当前列表中
print "------------"
list1 = [1,2,3]
list.append(list1)
foreachPrint(list)
# extend 逐一添加另一个列表的元素
print "------------"
list.extend(list1)
foreachPrint(list)
# insert 在指定索引前增加元素
print "------------"
list.insert(1,"b")
foreachPrint(list)

'''
修改元素
'''
# 直接通过下标修改
print "------------"
list[2] = True
foreachPrint(list)

'''
查找元素
'''
# in & not in
print "------------"
num = 2
if num in list:
    print "in"
else:
    print "not in"

if num not in list:
    print "tr"
else:
    print "fa"

# index & count 和字符串用法相同
print "------------"
print list.index(1,0,len(list)) # 在查找1时,python会将true转成1返回(true在1的前面) false也适用
print list.count(1)

'''
删除元素
'''
# del 根据下标进行删除
print "------------"
del list[0]
foreachPrint(list)
# pop 删除最后一个元素
print "------------"
list.pop()
foreachPrint(list)
# remove 根据元素的值进行删除
print "------------"
list.remove(1)
foreachPrint(list)

'''
排序
'''
# sort 正序
print "------------"
list.sort()
foreachPrint(list)
# reverse 倒序
print "------------"
list.reverse()
foreachPrint(list)

