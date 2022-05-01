#!/usr/bin/env python3

# continue语句
for letter in 'Python':
    if letter == 'h':
        continue
    print('当前字母 :', letter)
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('当前变量值 :', var)
print("Good bye!")
var = 10
while var > 0:
    var = var - 1
    if var == 5 or var == 8:
        continue
    print('当前值 :', var)
print("Good bye!")
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
