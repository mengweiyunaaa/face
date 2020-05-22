# 1.
def print_everything(*args):
    for count, thing in enumerate(args):
        print '{0} {1}'.format(count, thing)
        
print_everything('apple', 'banana', 'cabbage')
# 0. apple

# 1. banana

# 2. cabbage






# 2.新式类与经典类
# 新式类都有一个__new__的静态方法，它的原型是object.__new__(cls[, ...])
# 新式类是在创建的时候继承内置object对象（或者是从内置类型，如list,dict等），而经典类是直
# 接声明的。使用dir()方法也可以看出新式类中定义很多新的属性和方法，
# 而经典类就2个['__doc__','__module__']


# 3. 单例模式

# ​ 单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。

# __new__()在__init__()之前被调用，用于生成实例对象。利用这个方法和类的属性的特点可以实现设计模式的单例模式。单例模式是指创建唯一对象，单例模式设计的类只能实例
# 这个绝对常考啊.绝对要记住1~2个方法,当时面试官是让手写的.

# 1 使用__new__方法

# class Singleton(object):

#     def __new__(cls, *args, **kw):

#         if not hasattr(cls, '_instance'):

#             orig = super(Singleton, cls)

#             cls._instance = orig.__new__(cls, *args, **kw)

#         return cls._instance

 

# class MyClass(Singleton):

#     a = 1

# 2 共享属性

# 创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.

 

# class Borg(object):

#     _state = {}

#     def __new__(cls, *args, **kw):

#         ob = super(Borg, cls).__new__(cls, *args, **kw)

#         ob.__dict__ = cls._state

#         return ob

 

# class MyClass2(Borg):

#     a = 1

# 3 装饰器版本

# def singleton(cls):

#     instances = {}

#     def getinstance(*args, **kw):

#         if cls not in instances:

#             instances[cls] = cls(*args, **kw)

#         return instances[cls]

#     return getinstance

 

# @singleton

# class MyClass:

#   ...

# 4 import方法

# 作为python的模块是天然的单例模式

# # mysingleton.py

# class My_Singleton(object):

#     def foo(self):

#         pass

 

# my_singleton = My_Singleton()

 

# # to use

# from mysingleton import my_singleton

 

# my_singleton.foo()




# 4. Python中的作用域

# Python 中，一个变量的作用域总是由在代码中被赋值的地方所决定的。

# 当 Python 遇到一个变量的话他会按照这样的顺序进行搜索：

# 本地作用域（Local）→当前作用域被嵌入的本地作用域（Enclosing locals）→全局/模块作用域（Global）
# 内置作用域（Built-in）



# 5.GIL线程全局锁

# 线程全局锁(Global Interpreter Lock),即Python为了保证线程安全而采取的独立线程运行的限制,说白了就是一个核只能在同一时间运行一个线程.对于io密集型任务，python的多线程起到作用，但对于cpu密集型任务，python的多线程几乎占不到任何优势，还有可能因为争夺资源而变慢。

# 见Python 最难的问题

# 解决办法就是多进程和下面的协程(协程也只是单CPU,但是能减小切换代价提升性能).








# 6 .Python自省

# 这个也是python彪悍的特性.

# 自省就是面向对象的语言所写的程序在运行时,所能知道对象的类型.简单一句就是运行时能够获得对象的类型.比如type(),dir(),getattr(),hasattr(),isinstance().

# a = [1,2,3]

# b = {'a':1,'b':2,'c':3}

# c = True

# print type(a),type(b),type(c) # <type 'list'> <type 'dict'> <type 'bool'>

# print isinstance(a,list)  # True



# 7.字典推导式

# 可能你见过列表推导时,却没有见过字典推导式,在2.7中才加入的:

# d = {key: value for (key, value) in iterable}


# 8 字符串格式化:%和.format

# .format在许多方面看起来更便利.对于%最烦人的是它无法同时传递一个变量和元组.你可能会想下面的代码不会有什么问题:

# "hi there %s" % name

# 但是,如果name恰好是(1,2,3),它将会抛出一个TypeError异常.为了保证它总是正确的,你必须这样做:

# "hi there %s" % (name,)   # 提供一个单元素的数组而不是一个参数

# 但是有点丑..format就没有这些问题.你给的第二个问题也是这样,.format好看多了.

# 你为什么不用它?

# 不知道它(在读这个之前)
# 为了和Python2.5兼容(譬如logging库建议使用%(issue #4))




# 9 迭代器和生成器




# 问： 将列表生成式中[]改成() 之后数据结构是否改变？
# 答案：是，从列表变为生成器

# >>> L = [x*x for x in range(10)]

# >>> L

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# >>> g = (x*x for x in range(10))

# >>> g

#  at 0x0000028F8B774200>

# 通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，
# 创建一个包含百万元素的列表，不仅是占用很大的内存空间，如：我们只需要访问前面的几个元素，
# 后面大部分元素所占的空间都是浪费的。因此，没有必要创建完整的列表
# （节省大量内存空间）。在Python中，我们可以采用生成器：边循环，边计算的机制—>generator



# 10 面向切面编程AOP和装饰器

# 这个AOP一听起来有点懵,同学面阿里的时候就被问懵了…

# 装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、
# 性能测试、事务处理等。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出
# 大量函数中与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存
# 在的对象添加额外的功能。