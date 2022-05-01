#!/usr/bin/env python3

# 变量赋值
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1
a, b, c = 1, 2, "john"

# 数字
var1 = 1
var2 = 10
var3 = 10
del var1
del var2, var3
intValue = 51924361  # 有符号整型
floatValue = 32.3e+18  # 浮点型
complexValue = 9.322e-36j  # 复数

# 字符串
s = "a1a2···an"
s = 'abcdef'
print(s[1:5])
string = 'Hello World!'
print(string)  # 输出完整字符串
print(string[0])  # 输出字符串中的第一个字符
print(string[2:5])  # 输出字符串中第三个至第六个之间的字符串
print(string[2:])  # 输出从第三个字符开始的字符串
print(string * 2)  # 输出字符串两次
print(string + "TEST")  # 输出连接的字符串

# 列表
infoList = ['franklin', 786, 2.23, 'john', 70.2]
tinyList = [123, 'john']
print(infoList)  # 输出完整列表
print(infoList[0])  # 输出列表的第一个元素
print(infoList[1:3])  # 输出第二个至第三个元素
print(infoList[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinyList * 2)  # 输出列表两次
print(infoList + tinyList)  # 打印组合的列表

# 元组（相当于只读列表）
infoTuple = ('franklin', 786, 2.23, 'john', 70.2)
tinyTuple = (123, 'john')
print(infoTuple)  # 输出完整元组
print(infoTuple[0])  # 输出元组的第一个元素
print(infoTuple[1:3])  # 输出第二个至第四个（不包含）的元素
print(infoTuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinyTuple * 2)  # 输出元组两次
print(infoTuple + tinyTuple)  # 打印组合的元组
try:
    infoTuple[2] = 1000  # 元组中是非法应用
except Exception as e:
    print(e)
infoList[2] = 1000  # 列表中是合法应用

# 字典
infoDict = {}
infoDict['one'] = "This is one"
infoDict[2] = "This is two"
tinyDict = {'name': 'franklin', 'code': 6734, 'dept': 'sales'}
print(infoDict['one'])  # 输出键为'one' 的值
print(infoDict[2])  # 输出键为 2 的值
print(tinyDict)  # 输出完整的字典
print(tinyDict.keys())  # 输出所有键
print(tinyDict.values())  # 输出所有值

# 数据类型转换
int('100')  # 将字符串或数字转换为整型
int('12', 16)
int(3.6)
float(112)  # 将整数和字符串转换成浮点数
float('123')
complex(1, 2)  # 创建复数或者转化字符串为复数
complex("1+2j")
str(1234)  # 将对象转换为字符串
str({'baidu': 'baidu.com', 'google': 'google.com'})
repr('Microsoft')  # 将对象转换为表达式字符串
repr({'baidu': 'baidu.com', 'google': 'google.com'})
eval('pow(2,2)')  # 执行字符串的表达式，并返回表达式的值
a = 7
eval('3 * a')
tuple([1, 2, 3, 4])  # 将列表转换为元组。字典则转换为key组成的元组
tuple({1: 2, 3: 4})
list((123, 'franklin', 'google', 'abc'))  # 将元组转换为列表
x, y = set('baidu'), set('google')  # 转换为可变集合
print(x & y)  # 交集
print(x | y)  # 并集
print(x - y)  # 差集
dict(a='a', b='b', t='t')  # 创建字典
dict(zip(['one', 'two', 'three'], [1, 2, 3]))
dict([('one', 1), ('two', 2), ('three', 3)])
frozenset(range(10))  # 转换为不可变集合
frozenset('baidu')
chr(48)  # 将整数转换为字符
chr(0x30)
ord('a')  # 将字符转换为它的整数值
hex(255)  # 将整数转换为十六进制字符串
hex(-42)
oct(10)  # 将整数转换为八进制字符串
