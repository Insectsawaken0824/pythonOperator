# -*- coding:utf-8 -*-

# 读数据（readlines）
f = open("F://temp//readlines.txt","w")
i = 1
while i < 100000:
    f.write(str(i)+"\n")
    i += 1

ff = open("F://temp//readlines.txt", "r")
content = ff.readlines(8192)
for j in content:
    print j