#!/usr/bin/env python3

# 列表
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

# 访问列表中的值
print("list1[0]: {}".format(list1[0]))
print("list2[1:5]: {0}".format(list2[1:5]))

# 更新列表
list4 = []
list4.append('Google')  # 使用append()添加元素
list4.append('Franklin')

# 删除列表元素
print(list1)
del list1[2]
print("After deleting value at index 2 : ")
print(list1)

# 列表脚本操作符
print(len([1, 2, 3]))  # 长度
print([1, 2, 3] + [4, 5, 6])  # 组合
print(['Hi!'] * 4)  # 重复
print(3 in [1, 2, 3])  # 元素是否存在于列表中
for x in [1, 2, 3]:  # 迭代
    print(x)

# 列表截取
websites = ['Google', 'Baidu', 'Taobao']
print("websites[2]: {}".format(websites[2]))
print("websites[-2]: {0}".format(websites[-2]))
print("websites[1:]: {a}".format(a=websites[1:]))

# 列表函数与方法
print(len([7, 8, 9]))  # 列表元素个数
print(max([7, 8, 9]))  # 返回列表元素最大值
print(min([7, 8, 9]))  # 返回列表元素最小值
print(list((7, 8, 9)))  # 将元组转换为列表
list5 = ['a', 2, 'c']
list5.append(100)  # 在列表末尾添加新的对象
print(list5)
print(['a', 2, 'c', 2, 10].count(2))  # 统计某个元素在列表中出现的次数
list5.extend(['ext1', 10, 22, 10, 23])  # 在列表末尾一次性追加另一个序列中的多个值
print(list5)
print(['a', 2, 'c', 2, 10].index(2))  # 从列表中找出某个值第一个匹配项的索引位置
list5.insert(3, 2009)  # 将对象插入列表
print(list5)
print(['a', 2, 'c', 2, 10].pop())  # 移除列表中的一个元素（默认最后一个元素）且返回该元素的值
print(['a', 2, 'c', 2, 10].pop(2))
list5.remove(10)  # 移除列表中某个值的第一个匹配项
print(list5)
list5.reverse()  # 反向列表中元素
print(list5)
aList = ['123', 'Google', 'Taobao', 'Facebook']
aList.sort()  # 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
print(aList)
aList.sort(reverse=True)
print(aList)


def take_second(elem):  # 获取列表的第二个元素
    return elem[1]


random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=take_second)  # 指定第二个元素排序
print(random)
