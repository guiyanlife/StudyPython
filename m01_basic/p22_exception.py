#!/usr/bin/env python3
import os

# 标准异常
"""
BaseException  所有异常的基类
SystemExit  解释器请求退出
KeyboardInterrupt  用户中断执行（通常是输入^C）
Exception  常规错误的基类
StopIteration  迭代器没有更多的值
GeneratorExit  生成器(generator)发生异常来通知退出
StandardError  所有的内建标准异常的基类
ArithmeticError  所有数值计算错误的基类
FloatingPointError  浮点计算错误
OverflowError  数值运算超出最大限制
ZeroDivisionError  除（或取模）零（所有数据类型）
AssertionError  断言语句失败
AttributeError  对象没有这个属性
EOFError  没有内建输入，到达EOF标记
EnvironmentError  操作系统错误的基类
IOError  输入/输出操作失败
OSError  操作系统错误
WindowsError  系统调用失败
ImportError  导入模块/对象失败
LookupError  无效数据查询的基类
IndexError  序列中没有此索引(index)
KeyError  映射中没有这个键
MemoryError  内存溢出错误（对于Python解释器不是致命的）
NameError  未声明/初始化对象（没有属性）
UnboundLocalError  访问未初始化的本地变量
ReferenceError  弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError  一般的运行时错误
NotImplementedError  尚未实现的方法
SyntaxError  Python 语法错误
IndentationError  缩进错误
TabError  Tab 和空格混用
SystemError  一般的解释器系统错误
TypeError  对类型无效的操作
ValueError  传入无效的参数
UnicodeError  Unicode相关的错误
UnicodeDecodeError  Unicode解码时的错误
UnicodeEncodeError  Unicode编码时错误
UnicodeTranslateError  Unicode转换时错误
Warning  警告的基类
DeprecationWarning  关于被弃用的特征的警告
FutureWarning  关于构造将来语义会有改变的警告
OverflowWarning  旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning  关于特性将会被废弃的警告
RuntimeWarning  可疑的运行时行为(runtime behavior)的警告
SyntaxWarning  可疑的语法的警告
UserWarning  用户代码生成的警告
"""

# 异常处理
try:  # 正常的操作
    fh = open("testfile", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:  # 发生指定异常，执行这块代码
    print("Error: 没有找到文件或读取文件失败")
else:  # 如果没有异常执行这块代码
    print("内容写入文件成功")
    fh.close()

# 使用except而不带任何异常类型
try:
    fh = open("testfile", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except:  # 发生异常，执行这块代码
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

# 使用except而带多种异常类型
try:
    fh = open("testfile", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except (IOError, EOFError):
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

# try-finally语句
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:  # 无论是否发生异常都执行这段代码
    print("Error: 没有找到文件或读取文件失败")
    os.remove("testfile")

# 异常的参数
try:
    int("xyz")
except ValueError as arg:
    print("参数没有包含数字：", arg)

# 触发异常
try:
    raise Exception("raise exception by self")
except Exception as err:
    print(err)


# 用户自定义异常
class MyException(BaseException):
    def __init__(self, desc):
        self.desc = desc


try:
    raise MyException("raise my exception")
except MyException as err:
    print(err.desc)
