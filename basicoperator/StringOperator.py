# -*- coding:utf-8 -*-


# 字符串操作


name = "zhao tong chen"
# 索引
print name[6]
# 切片  格式:   [开始:结束:步长]
print name[2:7:2]
print name[2:]  # 索引2以后  包含2
print name[:2]  # 索引2以前  不包含2
print name[::2]  # 步长为2
print name[::-2]  # 步长为2 倒叙

# find() 返回开始的索引 没有返回-1  格式: 词,起始,截止
print name.find("ao",0,len(name))
# rfind() 从右边开始找
print name.rfind("ao",0,len(name))
# index() 返回开始的索引  没有报错 跟find用法一样
print name.index("ao",0,len(name))
# rindex() 从右边开始找
print name.rindex("ao",0,len(name))
# count() 返回关键词出现的次数 格式和find一样
print name.count("n",0,len(name))
# replace() 格式:(old,new,count) 旧串被新串替换,count是最大次数
print name.replace("h","Y",1)
# split() 格式(按照目标串切割,切割的最大次数)
print name.split("h",1)
# capitalize() 把字符串的首字母大写
print name.capitalize()
# title 把每个单词的首字母都大写
print name.title()
# startwith 检查字符串是否以目标开头
print name.startswith("zh")
# endswith 检查字符串是否以目标结束
print name.endswith("e")
# lower() 转成小写
print name.lower()
# upper() 转成大写
print name.upper()
# ljust() 左对齐,并使用空格填充至指定长度
print name.ljust(20)+"|"
# rjust() 左对齐,并使用空格填充至指定长度
print name.rjust(20)+"|"
# center() 居中,并使用空格填充至指定长度
print name.center(20)+"|"
# lstrip() 删除左边的空格
print name.lstrip()
# rstrip() 删除右边的空格
print name.rstrip()
# strip() 删除两边边的空格
print name.strip()
# partition() 以目标将字符串切割成三个部分
print name.partition("h")
# rpartition() 以目标将字符串切割成三个部分 从右边开始
print name.rpartition("h")
# splitlines() 按照行分割 返回一个包含各行元素的列表
print name.splitlines()
# isalpha() 判断串是否全部都是字母
print name.isalpha()
# isdigit() 判断串是否全部都是数字
print name.isdigit()
# isalnum() 判断串是否全部都是数字或字母
print name.isalnum()
# isspace() 判断串是否全部都是空格
print name.isspace()
# join() 跟每个字符串拼接 构造出新的字符串
li = ["hello", "world", "python"]
str = " - "
print str.join(li)

# 原始字符串
print "你\n好"
print r"你\n好"
# unicode 字符串
print u"你\n好"
