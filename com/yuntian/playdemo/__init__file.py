#!/usr/bin/python3

# 文件
from builtins import print,open
import chardet
import os


print('-------文件---------')
curPath = os.path.abspath(os.path.dirname(__file__))

print(curPath)

with open('resource/file/a.text', 'r', encoding='utf-8') as f:
    print(f.name)
    f_read=f.read()
    f_charInfo = chardet.detect(f_read.encode())
    print(f_charInfo)
    print(f_read)







