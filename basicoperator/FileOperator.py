# -*- coding:utf-8 -*-


# 打开文件
print "----------------"
f = open("C://Users//zhao//Desktop//16_09_special.txt", "r")



# 访问模式	说明
# r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# w	    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入
#         到已有内容之后。如果该文件不存在，创建新文件进行写入。
# rb	    以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# wb	    以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab	    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内
#         容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# r+	    打开一个文件用于读写。文件指针将会放在文件的开头。
# w+	    打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a+	    打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果
#         该文件不存在，创建新文件用于读写。
# rb+	    以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# wb+	    以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab+	    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，
#         创建新文件用于读写。


# 关闭文件
f.close()

# 文件的读写
# 写数据
print "----------------"
ff = open("C://Users//zhao//Desktop//pywrite.txt", "w")
ff.write("nihao \n nihao")
ff.close()

# 读数据(read)
# 如果open是打开一个文件，那么可以不用谢打开的模式，即只写 open('test.txt')
# 如果使用读了多次，那么后面读取的数据是从上次读完后的位置开始的
print "----------------"
ff = open("C://Users//zhao//Desktop//pywrite.txt", "r")
content = ff.read(2)
print(content)
content = ff.read()
print(content)
ff.close()

# 读数据（readlines）无参数
print "----------------"
f = open("F://temp//readlines.txt")
content = f.readlines()
print(type(content))
# 读数据（readlines）带参数
# readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行,
# 实际读取值可能比sizhint较大, 因为需要填充缓冲区。
# 如果碰到结束符 EOF 则返回空字符串。
# 实际上遇到的情况是这个sizeint参数只能是8192=2^13的整数倍返回的结果才会有变化
# 也就是说readlines(1)和readlines(8192)效果是一样的，但realines(8193)就不一样了。
ff = open("F://temp//readlines.txt", "r")
content = ff.readlines(8192)
for j in content:
    print j

i=1
for temp in content:
    print("%d:%s"%(i, temp))
    i+=1
f.close()

# 读数据（readline）
print "----------------"
f = open("C://Users//zhao//Desktop//pywrite.txt")
content = f.readline()
print("1:%s"%content)
content = f.readline()
print("2:%s"%content)
f.close()


# 获取当前读写的位置
# 打开一个已经存在的文件
print "----------------"
f = open("C://Users//zhao//Desktop//pywrite.txt")
str = f.read(3)
print "读取的数据是 : ", str
# 查找当前位置
position = f.tell()
print "当前文件位置 : ", position
str = f.read(3)
print "读取的数据是 : ", str
# 查找当前位置
position = f.tell()
print "当前文件位置 : ", position
f.close()


# 定位到某个位置

# seek(offset, from)有2个参数
#     offset:偏移量
#     from:方向
#         0:表示文件开头
#         1:表示当前位置
#         2:表示文件末尾

# 从文件开头，偏移5个字节
# 打开一个已经存在的文件
print "----------------"
f = open("C://Users//zhao//Desktop//pywrite.txt", "r")
str = f.read(30)
print "读取的数据是 : ", str
# 查找当前位置
position = f.tell()
print "当前文件位置 : ", position
# 重新设置位置
f.seek(5, 0)
# 查找当前位置
position = f.tell()
print "当前文件位置 : ", position
f.close()

# 离文件末尾，3字节处
# 打开一个已经存在的文件
print "----------------"
f = open("C://Users//zhao//Desktop//pywrite.txt", "r")
# 查找当前位置
position = f.tell()
print "当前文件位置 : ", position
# 重新设置位置
f.seek(-3,2)
# 读取到的数据为：文件最后3个字节数据
str = f.read()
print "读取的数据是 : ", str
f.close()