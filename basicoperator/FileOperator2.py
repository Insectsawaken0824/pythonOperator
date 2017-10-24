# -*- coding:utf-8 -*-

import os

'''
文件的重命名、删除
有些时候，需要对文件进行重命名、删除等一些操作
python的os模块中都有这么功能
'''
# 重命名
os.rename("C:\Users\zhao\Desktop\pywrite.txt","11-22")
# 删除
os.remove("11-22")


'''
文件夹相关操作
'''
# 创建文件夹
os.mkdir("张三")
# 获取当前目录
os.getcwd()
# 改变默认目录
os.chdir("../")
# 获取目录列表
os.listdir("./")
# 删除文件夹
os.rmdir("张三")