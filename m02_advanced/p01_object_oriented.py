#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 面向对象技术简介
"""
类(Class)：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖(override)，也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
继承：即一个派生类(derived class)继承基类(base class)的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
实例化：创建一个类的实例，类的具体对象。
方法：类中定义的函数。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
"""


# 创建类
class Employee:  # 实例
    """所有员工的基类"""  # 类文档字符串
    empCount = 0  # 类变量。在这个类的所有实例之间共享

    def __init__(self, name, salary):  # 构造函数
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_count(self):
        print("Total Employee %d" % Employee.empCount)

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


class Test:
    def prt(self):
        print(self)  # self代表类的实例，而非类
        print(self.__class__)


t = Test()
t.prt()


class Test1:
    def prt(google):  # self不是python关键字，换成google也可以正常执行
        print(google)
        print(google.__class__)


t1 = Test1()
t1.prt()

# 创建实例对象
emp1 = Employee("Zara", 2000)  # 通过 __init__ 方法接收参数
emp2 = Employee("Manni", 5000)

# 访问属性
emp1.display_employee()  # 使用点号.来访问对象的属性
emp2.display_employee()
print("Total Employee %d" % Employee.empCount)
emp1.age = 7  # 添加，修改，删除类的属性
emp1.age = 8
del emp1.age
hasattr(emp1, 'age')  # 检查是否存在指定属性
setattr(emp1, 'age', 8)  # 设置属性。如果属性不存在，会创建新属性
getattr(emp1, 'age')  # 访问对象的属性
delattr(emp1, 'age')  # 删除属性

# 内置类属性
print("Employee.__doc__:", Employee.__doc__)  # 类的文档字符串
print("Employee.__name__:", Employee.__name__)  # 类名
print("Employee.__module__:", Employee.__module__)  # 类定义所在的模块
print("Employee.__bases__:", Employee.__bases__)  # 类的所有父类构成元素（包含了一个由所有父类组成的元组）
print("Employee.__dict__:", Employee.__dict__)  # 类的属性（包含一个字典，由类的数据属性组成）

# 对象销毁（垃圾回收）
a = 40  # 创建对象
b = a  # 增加引用
c = [b]  # 增加引用
del a  # 减少引用
b = 100  # 减少引用
c[0] = -1  # 减少引用


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # 打印对象的id
del pt1
del pt2
del pt3


# 类的继承
class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parent_method(self):
        print('调用父类方法')

    def set_attr(self, attr):
        Parent.parentAttr = attr

    def get_attr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent):  # 定义子类
    def __init__(self):
        super().__init__()
        print("调用子类构造方法")

    def child_method(self):
        print('调用子类方法')


c = Child()  # 实例化子类
c.child_method()  # 调用子类的方法
c.parent_method()  # 调用父类方法
c.set_attr(200)  # 调用父类的方法，设置属性值
c.get_attr()  # 调用父类的方法，获取属性值
print(issubclass(c.__class__, Parent))  # 判断一个类是否是另一个类的子类或者子孙类
print(isinstance(c, Child))  # 判断一个实例是否是指定子类的实例对象


# 方法重写
class Parent:  # 定义父类
    def my_method(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def my_method(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.my_method()  # 子类调用重写方法

# 基础重载方法
"""
__init__(self[, args...])
构造函数
简单的调用方法：obj = className(args)

__del__(self)
析构方法，删除一个对象
简单的调用方法：del obj

__repr__(self)
转化为供解释器读取的形式
简单的调用方法：repr(obj)

__str__(self)
用于将值转化为适于人阅读的形式
简单的调用方法：str(obj)

__cmp__(self, x)
对象比较
简单的调用方法：cmp(obj, x)
"""


# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

# 类属性与方法
"""
类的私有属性
__private_attrs: 两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs

类的方法
在类的内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self且为第一个参数

类的私有方法
__private_method: 两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_method
"""


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
try:
    print(counter.__secretCount)  # 报错，实例不能访问私有变量
except AttributeError as e:
    print(e)
print(counter._JustCounter__secretCount)  # 可以使用object._className__attrName（对象名._类名__私有属性名）访问私有属性
"""
单下划线、双下划线、头尾双下划线说明：
__foo__: 定义的是特殊方法，一般是系统定义名字，类似__init__()之类的。
_foo: 以单下划线开头的表示的是protected类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于from module import *
__foo: 双下划线的表示的是私有类型private的变量，只能是允许这个类本身进行访问了。
"""
