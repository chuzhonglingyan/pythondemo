#!/usr/bin/python3
from builtins import print

# 函数
print('-------方法---------')


def hello():
    print('Hello World')


# 计算面积函数
def area(width, height):
    return width * height

hello()

w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
