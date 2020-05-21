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