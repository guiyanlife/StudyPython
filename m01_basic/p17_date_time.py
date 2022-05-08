#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import calendar
import os
from datetime import datetime
import time

# 时间
print(f"当前时间戳为：{time.time()}")

# 时间元组
"""
一个元组装起来的9组数字，用于处理时间。时间元祖(time.struct_time)的属性与含义如下：
tm_year   4位数年。0000~9999
tm_mon    月。1~12
tm_mday   日。1~31
tm_hour   小时。0~23
tm_min    分钟。0~59
tm_sec    秒。0~61（60或61是闰秒）
tm_wday   一周的第几日。0~6（0是周一）
tm_yday   一年的第几日。1~366（366闰年）
tm_isdst  1: 夏令时；0: 非夏令时；-1: 不确定
"""

# 获取当前时间
print(f"本地时间为：{time.localtime(time.time())}")

# 获取格式化的时间
print(f"本地时间为：{time.asctime(time.localtime(time.time()))}")

# 格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
print(time.mktime(time.strptime("Sat Mar 28 22:24:24 2016", "%a %b %d %H:%M:%S %Y")))
"""
时间日期格式化符号：
%y  两位数的年份表示(00-99)
%Y  四位数的年份表示(000-9999)
%m  月份(01-12)
%d  月内中的一天(0-31)
%H  24小时制小时数(0-23)
%I  12小时制小时数(01-12)
%M  分钟数(00-59)
%S  秒(00-59)
%a  本地简化星期名称
%A  本地完整星期名称
%b  本地简化的月份名称
%B  本地完整的月份名称
%c  本地相应的日期表示和时间表示
%j  年内的一天(001-366)
%p  本地A.M.或P.M.的等价符
%U  一年中的星期数(00-53)星期天为星期的开始
%w  星期(0-6)，星期天为星期的开始
%W  一年中的星期数(00-53)星期一为星期的开始
%x  本地相应的日期表示
%X  本地相应的时间表示
%Z  当前时区的名称
%%  %号本身
"""

# 获取某月日历
print("以下输出2016年1月份的日历：")
print(calendar.month(2016, 1))

# Time模块
print("time.altzone %d " % time.altzone)  # 返回格林威治西部的夏令时地区的偏移秒数
print("time.asctime(t): %s " % time.asctime(time.localtime()))  # 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"的24个字符的字符串
t0 = time.perf_counter()  # 以浮点数计算的秒数返回当前的CPU时间
time.sleep(1)  # 函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间
print(time.perf_counter() - t0, "seconds process time")
t0 = time.time()  # 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
time.sleep(1)
print(time.time() - t0, "seconds wall time")
print("time.ctime(): %s" % time.ctime())  # 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式
print(f"time.gmtime(): {time.gmtime()}")  # 将一个时间戳转换为UTC时区（0时区）的struct_time，可选的参数sec表示从1970年1月1日以来的秒数
print(f"time.localtime(): {time.localtime()}")  # 格式化时间戳为本地的时间。如果参数未输入，则以当前时间为转换标准
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
print(f"time.mktime(t): {time.mktime(t)}")  # 接收struct_time对象作为参数，返回用秒数来表示时间的浮点数
print(f"date and time: {datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}")  # 接收以时间元组，并返回以可读字符串表示的当地时间
print(f"返回的元组：{time.strptime('30 Nov 00', '%d %b %y')}")  # 根据指定的格式把一个时间字符串解析为时间元组
os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()  # 根据环境变量TZ重新初始化时间相关设置
print(time.strftime('%X %x %Z'))
"""
Time模块包含了以下2个重要的属性：
time.timezone  属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数。
time.tzname    属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称和不带的
"""

# 日历(Calendar)模块
"""
calendar.calendar(year, w=2, l=1, c=6)
返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。每日宽度间隔为w字符。每行长度为21*w+18+2*c。l是每星期行数
calendar.firstweekday()
返回当前每周起始日期的设置。默认情况下，首次载入calendar模块时返回0，即星期一
calendar.isleap(year)
是闰年返回True，否则为False
calendar.leapdays(y1, y2)
返回在y1, y2两年之间的闰年总数
calendar.month(year, month, w=2, l=1)
返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7*w+6。l是每星期的行数
calendar.monthcalendar(year ,month)
返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。year年month月外的日期都设为0；范围内的日子都由该月第几日表示，从1开始
calendar.monthrange(year ,month)
返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）；月从1到12
calendar.prcal(year, w=2, l=1, c=6)
相当于print(calendar.calendar(year, w=2, l=1, c=6))
calendar.prmonth(year,month,w=2,l=1)
相当于print(calendar.month(year,month,w=2,l=1))
calendar.setfirstweekday(weekday)
设置每周的起始日期码。0（星期一）到6（星期日）
calendar.timegm(tupletime)
和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）
calendar.weekday(year, month, day)
返回给定日期的日期码。0（星期一）到6（星期日）。月份为1（一月）到12（十二月）
"""

# 其他相关模块和函数
"""
其他处理日期和时间的模块还有：
datetime模块
pytz模块
dateutil模块
"""
