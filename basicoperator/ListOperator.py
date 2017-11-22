# -*- coding:utf-8 -*-

# python的列表可以存不同类型的数据
list = ["a", 1, False]
print list[0]
print list[1]
print list[2]

#######
# 遍历
#######
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

##########
# 添加操作
##########
# append 向列表追加元素 如果也是列表,则会把列表当做一个元素,加入到当前列表中
print "------append------"
list1 = [1,2,3]
list.append(list1)
print list
# extend 逐一添加另一个列表的元素 这个是对原有列表的扩展
# 对于列表的扩展 可以通过extend 相加 和 分片 三种操作进行
# extend和分片是对原来列表进行操作, 相加是返回一个新列表
# extend比分片操作代码可读性高
print "------extend------"
list.extend(list1)
print list
# insert 在指定索引前增加元素
print "------insert------"
list.insert(1,"b")
print list

##########
# 修改元素
##########
# 直接通过下标修改
print "------------"
list[2] = True
print list

##########
# 查找元素
##########
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

# count 和字符串用法相同
print "------index------"
print list.index(1,0,len(list)) # 在查找1时,python会将true转成1返回(true在1的前面) false也适用

##########
# 删除元素
##########
# del 根据下标进行删除
print "------del------"
del list[0]
print list
# pop 删除最后一个元素 并返回
# pop是唯一一个技能修改列表又返回元素值的列表方法
print "------pop------"
pop = list.pop()
print list
print pop
# remove 根据元素的值进行删除
# 移除列表中某个值的第一个匹配项
print "------remove------"
list.remove(1)
print list

##########
# 排序
##########
# sort 正序 更改列表
# 如果希望不更改列表有两种方法
# 第一种对原有列表的副本进行排序 副本: x[:]
# 第二种使用sorted函数
print "------sort------"
list.sort()
print list
# sort 带参数 key: 按照这个规则排序 reverse: 是否倒序 sorted函数也适用这两个参数
print "------sort 2------"
# list.sort(key=len,reverse=False)
print list
# reverse 倒序 方向迭代函数:reversed
print "------reverse------"
list.reverse()
print list

##########
# 统计
##########
print "------count------"
list = ['to', 'be', 'or', 'not', 'to', 'be']
print list.count('be')