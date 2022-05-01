#!/usr/bin/env python3

# while语句
count = 0
while count < 9:
    print('The count is:', count)
    count = count + 1
print("Good bye!")

# continue和break用法
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非偶数时跳过输出
        continue
    print(i)  # 输出偶数2, 4, 6, 8, 10
i = 1
while 1:  # 循环条件为1必定成立
    print(i)  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

# 无限循环
var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
    num = input("Enter a number  :")
    if num == 'quit':
        break
    else:
        print("You entered: ", num)
print("Good bye!")

# 循环使用else语句
count = 0
while count < 5:
    print(count, " is less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

# 简单语句组
flag = 1
while flag: print('Given flag is really true!')  # 可使用Ctrl+C来中断循环
print("Good bye!")
