#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 模块
"""
Python模块(Module)，是一个Python文件，以.py结尾，包含了Python对象定义和Python语句。
模块能够有逻辑地组织Python代码段
把相关的代码分配到一个模块里能让你的代码更好用，更易懂
模块能定义函数、类和变量，模块里也能包含可执行的代码
"""

# import语句
import p18_function  # 模块的引入

p18_function.print_me("调用模块p18_function内的print_me()函数")

# from…import语句
from p18_function import change_me  # 从模块中导入一个指定的部分到当前命名空间中

change_me([91, 92, 93])

# from…import*语句
from p18_function import *  # 把一个模块的所有内容全都导入到当前的命名空间

print_info("Lily")

# 搜索路径
"""
当导入一个模块，Python解析器对模块位置的搜索顺序是：
1. 当前目录
2. 如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录
3. 如果都找不到，Python会查看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录
"""

# PYTHONPATH变量
"""
作为环境变量，PYTHONPATH由装在一个列表里的许多目录组成。PYTHONPATH的语法和shell变量PATH的一样
在Windows系统，典型的PYTHONPATH如下：
set PYTHONPATH=c:\python27\lib;
在UNIX系统，典型的PYTHONPATH如下：
set PYTHONPATH=/usr/local/lib/python
"""

# 命名空间和作用域
money = 2000


def add_money():
    global money  # 给函数内的全局变量赋值，须使用global语句
    money = money + 1


print(money)
add_money()
print(money)

# dir()函数
import math

print(dir(math))  # 返回的列表容纳了在一个模块里定义的所有模块、变量和函数

# globals()和locals()函数
print(globals())  # 以字典类型返回当前位置的全部全局变量
print(locals())  # 以字典类型返回当前位置的全部局部变量

# reload()函数
import importlib

importlib.reload(math)  # 重新载入模块

# Python中的包
from package_python.python1 import python1
from package_python.python2 import python2

python1()
python2()
