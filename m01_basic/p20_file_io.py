#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os

# 打印到屏幕
print("Python是一个非常棒的语言，不是吗？")

# 读取键盘输入
input_str = input("请输入：")
print("你输入的内容是: ", input_str)

# 打开和关闭文件
fo = open("foo.txt", "w")  # 打开一个文件
print("文件名：{0}".format(fo.name))
print("是否已关闭：{0}".format(fo.closed))
print("访问模式：{0}".format(fo.mode))
fo.write("www.google.com!\nVery good site!\n")  # 写入字符串到打开的文件
fo.close()  # 关闭打开的文件
fo = open("foo.txt", "r")
print("读取的字符串是：{0}".format(fo.read(10)))  # 从打开的文件中读取字符串
fo.close()

# 文件定位
fo = open("foo.txt", "r+")
print("读取的字符串是：{0}".format(fo.read(6)))
print("当前文件位置：{0}".format(fo.tell()))  # 获取当前内文件位置
position = fo.seek(0, 0)  # 把指针再次重新定位到文件开头
print("重新读取字符串：{0}".format(fo.read(6)))
fo.close()

# 重命名和删除文件
os.rename("foo.txt", "foo1.txt")  # 重命名文件
os.remove("foo1.txt")  # 删除文件

# 目录
os.mkdir("test_dir")  # 创建目录
os.rmdir("test_dir")  # 删除目录
print("当前目录：{0}".format(os.getcwd()))  # 显示当前工作目录
os.chdir("..")  # 改变当前工作目录
print("当前目录：{0}".format(os.getcwd()))

# 文件、目录相关的方法
"""
File对象和OS对象提供了很多文件与目录的操作方法
"""
