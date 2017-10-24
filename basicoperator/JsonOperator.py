# -*- coding:utf-8 -*-

import json

readFile = open("C:\Users\zhao\Documents\Tencent Files//173173666\FileRecv//a.txt","r")
readlines = readFile.readlines()
for line in readlines:
    jsonObj = json.loads(line)
    jb_list = jsonObj["searchIndexs"]["lists"]
    for jb in jb_list:
        print jb["id"]
