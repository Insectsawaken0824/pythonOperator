# -*- coding:utf-8 -*-

# 字典类似Java的Map
dic = {"name":"小明","age":"18","gender":"男"}

# 获取值
print dic.get("name")

# 修改值
dic["name"] = "小刚"
print dic.get("name")

# 添加新元素
dic["phone"] = 1333333333
print dic.get("phone")

# 删除元素
# del 删除元素或整个字典
del dic["phone"]
# clear 清空字典
dic.clear()

# len 键值对个数
len(dic)

# keys 包含所有key的列表
dic.keys()

# 返回一个包含所有（键，值）元祖的列表
dic.items()

# dict.has_key(key)如果key在字典中，返回True，否则返回False
dic.has_key("name")

'''
遍历
'''
dic = {"name":"小明","age":"18","gender":"男"}
# 遍历字典的key（键）
print "--------------"
for key in dic.keys():
    print key
# 遍历字典的value（值）
print "--------------"
for value in dic.values():
    print value
# 遍历字典的项（元素）
print "--------------"
for item in dic.items():
    print item
# 遍历字典的key - value（键值对）
print "--------------"
for k,v in dic.items():
    print "key=%s,value=%s"%(k,v)
# 带下标的遍历
