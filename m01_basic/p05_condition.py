#!/usr/bin/env python3

# if基本用法
flag = False
name = 'guiyan'
if name == 'python':  # 判断变量是否为 python
    flag = True  # 条件成立时设置标志为真
    print("welcome boss")  # 并输出欢迎信息
else:
    print(name)  # 条件不成立时输出变量名称

# elif用法
num = 5
if num == 3:  # 判断num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:  # 值小于零时输出
    print('error')
else:
    print('passerby')  # 条件均不成立时输出

# if语句多个条件
num = 9
if 0 <= num <= 10:  # 判断值是否在0~10之间
    print('hello')
num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print('hello')
else:
    print('undefine')
num = 8
if (0 <= num <= 5) or (num >= 10 and num <= 15):  # 判断值是否在0~5或者10~15之间
    print('hello')
else:
    print('undefine')

# 简单语句组
var = 100
if var == 100: print("变量 var 的值为100")
print("Good bye!")
