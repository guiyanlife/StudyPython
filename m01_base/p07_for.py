#!/usr/bin/env python3

# for循环语句
for letter in 'Python':
    print("当前字母: %s" % letter)
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('当前水果: %s' % fruit)
print("Good bye!")

# 通过序列索引迭代
for index in range(len(fruits)):
    print('当前水果 : %s' % fruits[index])
print("Good bye!")

# 循环使用else语句
for num in range(10, 20):  # 迭代10到20之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的else部分
        print('%d 是一个质数' % num)
