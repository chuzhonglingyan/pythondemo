#!/usr/bin/python3
from builtins import print, set, type, int, input

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数


print('-------斐波纳契数列---------')
a, b = 0, 1

while b<10:
    print(b, end=',')
    a,b=b,a+b

print('-------条件语句---------')
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)
### 退出提示
input("点击 enter 键退出")



num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")


