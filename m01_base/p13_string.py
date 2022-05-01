#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 字符串
var1 = 'Hello World!'
var2 = "Python"

# 访问字符串中的值
print(f"var1[0]: {var1[0]}")
print(f"var2[1:5]: {var2[1:5]}")

# 字符串连接
var3 = var1[:6] + 'Franklin!'
print(f"输出 :- {var3}")

# 转义字符
"""
\   续行符（在行尾时）
\\  反斜杠符号
\'  单引号
\"  双引号
\a  响铃
\b  退格
\000  空
\n  换行
\v  纵向制表符
\t  横向制表符
\r  回车
\f  换页
\377    八进制数
\xFF    十六进制数
\other  其它的字符以普通格式输出
"""

# 字符串运算符
a = "Hello"
b = "Python"
print("a + b 输出结果：", a + b)  # 字符串连接
print("a * 2 输出结果：", a * 2)  # 重复输出字符串
print("a[1] 输出结果：", a[1])  # 通过索引获取字符串中字符
print("a[1:4] 输出结果：", a[1:4])  # 截取字符串中的一部分
if "H" in a:  # 成员运算符
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")
if "M" not in a:
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")
print(r'\n')  # 原始字符串
print(R'\n')
print("%s %s!" % (a, b))  # 格式字符串

# 字符串格式化
print("My name is %s and weight is %d kg!" % ('Zara', 21))
"""
字符串格式化符号：
%c  格式化字符及其ASCII码
%s  格式化字符串
%d  格式化整数
%u  格式化无符号整型
%o  格式化无符号八进制数
%x  格式化无符号十六进制数
%X  格式化无符号十六进制数（大写）
%f  格式化浮点数字，可指定小数点后的精度
%e  用科学计数法格式化浮点数
%E  作用同%e，用科学计数法格式化浮点数
%g  %f和%e的简写
%G  %F和%E的简写
%p  用十六进制数格式化变量的地址

格式化操作符辅助指令：
*  定义宽度或者小数点精度
-  用做左对齐
+  在正数前面显示加号(+)
<sp>  在正数前面显示空格
#  在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'（取决于用的是'x'还是'X'）
0  显示的数字前面填充'0'而不是默认的空格
%  '%%'输出一个单一的'%'
(var)  映射变量（字典参数）
m.n.  m 是显示的最小总宽度，n是小数点后的位数（如果可用的话）
"""

# format格式化函数
print("{} {}".format("hello", "world"))  # 默认顺序
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
print("网站名：{name}，地址：{url}".format(name="谷歌", url="www.google.com"))
site = {"name": "谷歌", "url": "www.google.com"}  # 通过字典设置参数
print("网站名：{name}，地址：{url}".format(**site))
my_list = ['谷歌', 'www.google.com']  # 通过列表索引设置参数
print("网站名：{0[0]}，地址：{0[1]}".format(my_list))


class AssignValue(object):
    def __init__(self, value):
        self.value = value


my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # 通过对象设置参数
print("{:.2f}".format(3.1415926))  # 数字格式化
print("{} 对应的位置是 {{0}}".format("Franklin"))  # 使用大括号{}来转义大括号

# 三引号
'''hi 
there'''  # 三引号允许一个字符串跨多行
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
sqlCmd = '''
CREATE TABLE users (  
login VARCHAR(8), 
uid INTEGER,
users.prid INTEGER)
'''

# Unicode字符串
print(u'Hello World!')
print(u'Hello\u0020World!')

# 字符串内建函数
print("hello!".capitalize())  # 把字符串的第一个字符大写
print("hello".center(20))  # 把字符串的第一个字符大写
print("hello".count("l"))  # 返回指定内容在字符串里面出现的次数
print("hello".count("l", 0, 3))
strEncode = "Google".encode('UTF-8', 'strict')  # 以指定的编码格式编解码字符串
print(strEncode.decode(encoding='UTF-8', errors='strict'))
print("Google".endswith("le"))  # 检查字符串是否以指定内容结束
print("Google".endswith("g", 0, 4))
print("abc\t12345\tdef".expandtabs())  # 把字符串中的tab符号转为（默认8个）空格
print("Googl\te".expandtabs(tabsize=6))
print('abca'.find('a'))  # 返回子字符串开始的索引值
print('abca'.find('a', 1))
print('abca'.find('3'))
print("{} {}".format("hello", "world"))  # 格式化字符串
print("{1} {0} {1}".format("hello", "world"))
print("string example".index("exam"))  # 返回子字符串开始的索引值，如果不存在报异常
print("string example".index("exam", 7))
try:
    print("string example".index("exam", 8))
except ValueError as e:
    print(e)
print("this2009".isalnum())  # 检测字符串是否由字母和数字组成
print("this is string".isalnum())
print("string0".isalpha())  # 检测字符串是否只由字母组成
print("12A".isdecimal())  # 检查字符串是否只包含十进制字符
print("999".isdecimal())
print("123".isdigit())  # 检测字符串是否只由数字组成
print("1b2".isdigit())
print("abc".islower())  # 检测字符串是否由小写字母组成
print("aBc".islower())
print(u"123".isnumeric())  # 检测字符串是否只由数字组成。这种方法是只针对unicode对象
print("    ".isspace())  # 检测字符串是否只由空格组成
print("This Is String Example".istitle())  # 检测字符串中所有的单词拼写首字母是否为大写且其他字母为小写
print("This is string example".istitle())
print("AAA".isupper())  # 检测字符串中所有的字母是否都为大写
print("-".join(("a", "b", "c")))  # 将序列中的元素以指定的字符连接生成一个新的字符串
print("this is string".ljust(50, '0'))  # 返回一个原字符串左对齐，默认使用空格填充至指定长度的新字符串
print("THIS IS STrING".lower())  # 转换字符串中所有大写字符为小写
print("     google".lstrip())  # 返回截掉字符串左边的空格或指定字符后生成的新字符串
trans = str.maketrans("aeiou", "12345")  # 创建字符映射的转换表
print("this is string example".translate(trans))
print(max("abcwfg"))  # 返回字符串中最大的字母
print(min("wbcafg"))  # 返回字符串中最小的字母
print("www.google.com".partition("."))  # 根据指定的分隔符将字符串进行分割
print("this is string example".replace("is", "Is"))  # 把字符串中的旧字符串替换成新字符串
print("this is string example".rfind("is"))  # 返回字符串最后一次出现的位置
print("this is string example".rindex("is"))  # 返回指定内容在字符串中最后出现的位置
print("this is string".rjust(50))  # 返回一个原字符串右对齐，默认使用空格填充至指定长度的新字符串
print("this is string".rjust(50, '0'))
print("www.google.com".rpartition("."))  # 从右边开始根据指定的分隔符将字符串进行分割
print("hello       ".rstrip() + "Franklin")  # 删除字符串末尾的空格
print("Google#Taobao#Facebook".split("#"))  # 通过指定分隔符对字符串进行切片
print("Google#Taobao#Facebook".split("#", 1))
print('ab c\n\nde fg\rkl\r\n'.splitlines())  # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表
print("this is string".startswith('this'))  # 检查字符串是否是以指定子字符串开头
print("begin" + "  center       ".strip() + "end")  # 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
print("Good Evening!".swapcase())  # 对字符串的大小写字母进行转换
print("this is string".title())  # 返回标题化的字符串
print("Good Evening!".translate(trans))  # 根据参数table给出的表转换字符串的字符，要过滤掉的字符放到del参数中
print("this is string".upper())  # 将字符串中的小写字母转为大写字母
print("this is string".zfill(40))  # 返回指定长度的字符串，原字符串右对齐，前面填充0
