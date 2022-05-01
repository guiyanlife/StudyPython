#!/usr/bin/env python3

# break语句
for letter in 'Python':
    if letter == 'h':
        break
    print('当前字母 :', letter)
var = 10
while var > 0:
    print('当前变量值 :', var)
    var = var - 1
    if var == 5:  # 当变量var等于5时退出循环
        break
print("Good bye!")
