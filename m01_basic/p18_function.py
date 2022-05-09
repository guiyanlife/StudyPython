#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 函数
def print_me(string):
    """打印传入的字符串到标准显示设备上"""
    print(string)
    return


print_me("我要调用用户自定义函数！")
print_me("再次调用同一函数")

# 参数传递
a = [1, 2, 3]  # 可修改的对象
a = "Google"  # 不可更改的对象


def change_int(num):  # 传不可变对象实例
    num = 10


b = 2
change_int(b)
print(b)


def change_me(my_list):  # 传可变对象实例
    """修改传入的列表"""
    my_list.append([1, 2, 3, 4])
    print(f"函数内取值：{my_list}")
    return


mylist = [10, 20, 30]
change_me(mylist)
print(f"函数外取值：{mylist}")

# 参数
try:
    print_me()  # 必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
except TypeError as e:
    print(e)


def print_info(name, age=35):
    """打印任何传入的字符串"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    return


print_info(age=50, name="Franklin")  # 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值
print_me(string="My string")
print_info(name="Lily")  # 默认参数的值如果没有传入，则被认为是默认值


def print_infos(arg1, *var_tuple):  # 不定长参数，加了星号*的变量名会存放所有未命名的变量参数
    """打印任何传入的参数"""
    print(f"输出: {arg1}")
    for var in var_tuple:
        print(var)
    return


print_infos(10)
print_infos(70, 60, 50)

# 匿名函数
sum_func = lambda arg1, arg2: arg1 + arg2
print("相加后的值为：{0}".format(sum_func(10, 20)))
print("相加后的值为：{0}".format(sum_func(20, 20)))


# return语句
def sum_function(arg1, arg2):
    """返回2个参数的和"""
    total = arg1 + arg2
    print("函数内：{0}".format(total))
    return total


print(sum_function(10, 20))

# 变量作用域
total = 0  # 全局变量


def sum_fun(arg1, arg2):
    total = arg1 + arg2  # 局部变量
    print("函数内是局部变量：{0}".format(total))
    return total


sum_fun(10, 20)
print("函数外是全局变量：{0}".format(total))
