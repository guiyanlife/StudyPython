#!/usr/bin/env python3

# 字典
tinyDict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}  # 字典的每个键值key:value对用冒号分割，每个键值对之间用逗号分割，整个字典包括在花括号中
tinyDict1 = {'abc': 456}
tinyDict2 = {'abc': 123, 98.6: 37}
tinyDict = {'a': 1, 'b': 2, 'b': '3'}  # 如果重复最后的一个键值对会替换前面的，值不需要唯一
print(tinyDict['b'])

# 访问字典里的值
tinyDict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("tinyDict['Name']: ", tinyDict['Name'])
print("tinyDict['Age']: ", tinyDict['Age'])
try:
    print("tinyDict['Alice']: ", tinyDict['Alice'])  # 如果用字典里没有的键访问数据，会输出错误
except KeyError as e:
    print(f"KeyError: {e}")

# 修改字典
tinyDict['Age'] = 8  # 更新
tinyDict['School'] = "Google"  # 添加
print("tinyDict['Age']: ", tinyDict['Age'])
print("tinyDict['School']: ", tinyDict['School'])

# 删除字典元素
print(tinyDict)
del tinyDict['Name']  # 删除键是Name的条目
print(tinyDict)
tinyDict.clear()  # 清空字典所有条目
print(tinyDict)
del tinyDict  # 删除字典
try:
    print(tinyDict)  # 删除字典后，字典不存在，引发异常
except NameError as e:
    print(e)

# 字典键的特性
tinyDict = {'Name': 'Franklin', 'Age': 7, 'Name': 'Manni'}  # 如果同一个键被赋值两次，后一个值会被记住
print("tinyDict['Name']: ", tinyDict['Name'])
try:
    tinyDict = {['Name']: 'Zara', 'Age': 7}  # 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
except TypeError as e:
    print(e)

# 字典内置函数与方法
tinyDict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(len(tinyDict))  # 计算字典元素个数，即键的总数
print(str(tinyDict))  # 输出字典可打印的字符串表示
print(type(tinyDict))  # 返回输入的变量类型，如果变量是字典就返回字典类型
tinyDict1 = tinyDict.copy()  # 返回字典的浅复制
tinyDict['Name'] = 'Google'
print(tinyDict)
print(tinyDict1)
print(dict.fromkeys(('Google', 'Taobao')))  # 创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
print(dict.fromkeys(('Google', 'Taobao'), 10))
print(tinyDict.get('Name'))  # 返回指定键的值，如果值不在字典中返回默认值
print(tinyDict.get('Name1', 'defaultName'))  # 返回指定键的值，如果值不在字典中返回默认值
print(tinyDict.items())  # 以列表返回可遍历的(key, value)元组数组
print(tinyDict.keys())  # 以列表返回一个字典所有的键
tinyDict.setdefault('NewName', 'newName')  # 如果键不存在于字典中，将会添加键并将值设为默认值
tinyDict.setdefault('Name', 'updateName')  # 如果键存在于字典中，则不更新
print(tinyDict)
tinyDict.update({'Name': 'ZaraNew'})  # 把字典dict2的键值对更新到dict里
print(tinyDict)
site = {'name': '谷歌', 'alexa': 10000, 'url': 'www.google.com'}
element = site.pop('name')  # 删除字典给定键key所对应的值，返回值为被删除的值
print('删除的元素为:', element)
print('字典为:', site)
element = site.popitem()  # 返回并删除字典中的最后一对键和值
print('删除的元素为:', element)
print('字典为:', site)
tinyDict.clear()  # 删除字典内所有元素
print(tinyDict)
