#!/usr/bin/env python3
import math
import cmath
import random

# 数字
var1 = 1
var2 = 10
var3 = 10
del var1
del var2, var3
intValue = -0xDEFABCECBDAECBFBAE  # 有符号整型
floatValue = -32.54e100  # 浮点型
complexValue = -.6545 + 0J  # 复数

# 类型转换
int("25")  # 转换为整数
float(10)  # 转换为浮点数
complex(3, 4)  # 创建复数
str(5678)  # 将对象转换为字符串
repr('Baidu')  # 将对象转换为表达式字符串
eval('3 * 3')  # 用来计算在字符串中的有效Python表达式，并返回一个对象
tuple([7, 8, 9, 10])  # 将列表转换为元组
list((1, 2, 3, 4, 5))  # 将序列转换为列表
chr(49)  # 将整数转换为字符
ord('b')  # 将字符转换为它的整数值
hex(255)  # 将整数转换为十六进制字符串
oct(20)  # 将整数转换为八进制字符串

# cmath模块
print(dir(cmath))
print(cmath.sqrt(-1))
print(cmath.sqrt(9))
print(cmath.sin(1))
print(cmath.log10(100))

# 数学函数
print(abs(-24.6))  # 返回数字的绝对值
print(math.ceil(5.1))  # 返回数字的上入整数
print(math.floor(5.9))  # 返回数字的下舍整数
print(math.exp(10))  # 返回e的指定次幂
print(math.fabs(-20))  # 返回数字的绝对值，以浮点型表示
print(math.log(math.e))  # 返回自然对数
print(math.log10(10))  # 返回以10为基数的对数
print(max(2, 3, 8, 1, 4))  # 返回指定参数的最大值
print(min(9, 10, 1, 21, 22))  # 返回指定参数的最小值
print(math.modf(99.123))  # 返回参数的整数部分与小数部分，两部分的数值符号与参数相同，整数部分以浮点型表示
print(pow(2, 4))  # 返回（x的y次方）的值
print(round(45.4987654))  # 返回浮点数的四舍五入值
print(round(45.4987654, 4))
print(math.sqrt(100))  # 返回数字的平方根

# 随机数函数
print(random.choice([1, 2, 3, 4, 5, 6]))  # 从序列的元素中随机挑选一个元素
print(random.randrange(49))  # 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为1
print(random.randrange(10, 49))
print(random.randrange(10, 49, 2))
print(random.random())  # 在[0,1)范围内随机生成实数
random.seed(10)  # 改变随机数生成器的种子
numList = [20, 16, 10, 5]
random.shuffle(numList)  # 将序列的所有元素随机排序
print(numList)
print(random.uniform(15, 25))  # 随机生成下一个实数，它在[x,y]范围内

# 三角函数
print(math.acos(-1))  # 返回反余弦弧度值
print(math.asin(1))  # 返回反正弦弧度值
print(math.atan(math.inf))  # 返回反正切弧度值
print(math.atan2(1, 0))  # 返回给定的坐标值(y,x)的反正切值
print(math.cos(math.pi))  # 返回弧度的余弦值
print(math.hypot(3, 4))  # 返回欧几里德范数sqrt(x*x+y*y)
print(math.sin(math.pi / 2))  # 返回的弧度的正弦值
print(math.tan(math.pi / 4))  # 返回弧度的正切值
print(math.degrees(math.pi / 2))  # 将弧度转换为角度
print(math.radians(180))  # 将角度转换为弧度

# 数学常量
print(math.pi)
print(math.e)
