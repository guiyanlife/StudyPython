#!/usr/bin/env python3

# 元组
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
tup4 = ()  # 空元组
tup5 = (50,)  # 元组中只包含一个元素时，需要在元素后面添加逗号

# 访问元组
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 修改元组
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
try:
    tup1[0] = 100  # 修改元组元素操作是非法的
except TypeError as e:
    print(e)
tup3 = tup1 + tup2
print(tup3)

# 删除元组
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup  # 元组中的元素值是不允许删除的，但可以删除整个元组
print("After deleting tup : ")
try:
    print(tup)  # 元组被删除后，输出变量会有异常信息
except NameError as e:
    print(e)

# 元组运算符
print(len((1, 2, 3)))  # 计算元素个数
print((1, 2, 3) + (4, 5, 6))  # 连接
print(('Hi!',) * 4)  # 复制
print(3 in (1, 2, 3))  # 元素是否存在
for x in (1, 2, 3):  # 迭代
    print(x, )

# 元组索引与截取
tup = ('spam', 'Spam', 'SPAM!')
print(tup[2])  # 读取第三个元素
print(tup[-2])  # 反向读取，读取倒数第二个元素
print(tup[-1:])  # 截取元素

# 无关闭分隔符
tup = 'abc', -4.24e93, 18 + 6.6j, 'xyz'  # 任意无符号的对象，以逗号隔开，默认为元组
print(tup)
x, y = 1, 2
print("Value of x, y : {0}, {1}".format(x, y))

# 元组内置函数
tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print("First tuple length : ", len(tuple1))  # 计算元组元素个数
print("Second tuple length : ", len(tuple2))
tuple1, tuple2 = ('123', 'xyz', 'zara', 'abc'), (456, 700, 200)
print("Max value element : ", max(tuple1))  # 返回元组中元素最大值
print("Max value element : ", max(tuple2))
print("Min value element : ", min(tuple1))  # 返回元组中元素最小值
print("Min value element : ", min(tuple2))
print(tuple((1, 2, 3, 4)))  # 将列表转换为元组
print(tuple({1: 2, 3: 4}))  # 针对字典，会返回字典的key组成的元组
