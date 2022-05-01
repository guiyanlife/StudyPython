#!/usr/bin/env python3

# 行和缩进
if True:
    print("True")
else:
    print("False")

# 多行语句
total = 1 + \
        2 + \
        3
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

# 引号
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

# 注释
# 第一个注释
print("Hello, Python!")  # 第二个注释
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''
"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# 空行。用于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

# 等待用户输入
input("按下 enter 键退出，其他任意键显示...\n")

# 同一行显示多条语句
a = 'a'; a = 'b'; print(a + " + " + a)

# print输出
x = "x"
y = "y"
print(x)  # 换行输出
print(y)
print('---------')
print(x, end="")  # 不换行输出
print(y, end="")
print(x, y)

# 多个语句构成代码组
value = 3
if value < 0:
    print("负数")
elif value == 0:
    print("0")
else:
    print("正数")
