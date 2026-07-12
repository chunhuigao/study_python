# Python 的可变类型和不可变类型有哪些

## 可变类型

    dict list set bytearray

## 不可变类型

    int float str tuple

# list、tuple、set、dict 的区别？

## list 列表

    列表是一种有序变的集合，可以存储任意类型的数据。
    列表的元素可以是其他列表、元组、字典等。
    列表的索引从 0 开始，每个元素都有一个唯一的索引

## tuple 元组

    元组是一种有序变的集合，可以存储任意类型的数据。
    元组的元素不能被修改，只能通过索引访问。
    元组的索引从 0 开始，每个元素都有一个唯一的索引
    元组的元素可以是其他元组、列表、字典等。

## set 集合

    集合是一种无序变的集合，不能存储重复的元素。
    集合的元素不能被修改，只能通过删除操作。
    集合的元素不能是可变类型，只能是不可变类型。
    集合的元素不能是 None。
    集合的元素不能是字典。

## dict 字典

    字典是一种无序变的集合，可以存储任意类型的数据。
    字典的键必须是不可变类型，值可以是任意类型。
    字典的键值对之间用逗号隔开，每个键值对之间用冒号隔开。
    字典的键值对之间用花括号括起来。
    字典的键值对之间用逗号隔开。
    字典的键值对之间用花括号括起来。

# is 和 == 的区别？

is 操作符用于判断两个变量是否指向同一个对象。
== 操作符用于判断两个变量的值是否相等。

# 深拷贝和浅拷贝有什么区别？

    浅拷贝：只复制对象的引用，不复制对象的内容。
    深拷贝：复制对象的内容，包括嵌套的对象。

# 如何实现深拷贝和浅拷贝

## 深拷贝

    import copy
    new_obj = copy.deepcopy(obj)
    print(new_obj)
    print(id(new_obj))

## 浅拷贝

    new_obj = copy.copy(obj)
    print(new_obj)
    print(id(new_obj))

# Python 的垃圾回收机制是什么？

    Python 的垃圾回收机制是一种自动管理内存的机制。
    它通过引用计数和循环引用检测来实现内存的自动回收。

# 什么是 GIL？它对多线程有什么影响？

GIL 是什么？
CPython 的全局互斥锁，同一时刻只允许一个线程执行 Python 字节码

为什么需要？
保护引用计数等内存管理机制的线程安全

对多线程的影响：
CPU 密集型 → 多线程无法并行，甚至更慢（串行 + 切换开销）
I/O 密集型 → 多线程有效（I/O 时释放 GIL）

绕过方案：
CPU 密集型 → multiprocessing / C扩展释放GIL
I/O 密集型 → 多线程 / asyncio

面试一句话：
"GIL 是 CPython 的全局解释器锁，保证同一时刻只有一个线程执行字节码，
导致 CPU 密集型任务无法并行，但 I/O 密集型任务不受影响。
CPU 密集型可用多进程绕过，I/O 密集型可用多线程或协程。"

# 装饰器是什么？怎么实现？

装饰器是一种在函数或类定义前添加代码的机制。
它可以在不修改原函数或类的情况下，为其添加新的功能。

装饰器的实现原理是：

1. 定义一个函数，该函数作为装饰器。
2. 装饰器函数的参数是需要装饰的函数或类。
3. 装饰器函数返回一个新的函数或类，该函数或类就是装饰后的函数或类。
4. 装饰后的函数或类在调用时，会先调用装饰器函数，再调用原函数或类。

# 生成器和迭代器的区别？

## 生成器

    生成器是一种特殊的迭代器，它可以生成一个无限序列的元素。
    生成器的元素是按需生成的，而不是一次性生成所有元素。
    生成器的元素可以是任意类型的数据，包括列表、元组、字典等。

# \*args 和 \*\*kwargs 的作用？

    *args 和 **kwargs 是 Python 中的特殊参数，用于在函数定义中接收任意数量的参数。
    *args 是一个元组，用于接收任意数量的非命名参数。
    **kwargs 是一个字典，用于接收任意数量的命名参数。
    这两个参数都可以在函数定义中使用，也可以在函数调用中使用。

# with 语句和上下文管理器是什么？

    with 语句是一种上下文管理器，用于在代码块执行前后自动管理资源。
    上下文管理器是一种协议，用于在代码块执行前后自动执行一些操作。
    上下文管理器的实现原理是：
    1. 定义一个类，该类作为上下文管理器。
    2. 类的 \_\enter\_\_ 方法在代码块执行前调用，用于初始化资源。
    3. 类的 \_\exit\_\_ 方法在代码块执行后调用，用于清理资源。

# Python 中类方法、静态方法、实例方法的区别？

实例方法 → 第一个参数 self → 操作实例数据 → 最常用
类方法 → 第一个参数 cls → 操作类数据 / 工厂方法 → @classmethod
静态方法 → 无特殊参数 → 与类相关的工具函数 → @staticmethod

面试一句话：
"实例方法通过 self 访问实例属性，类方法通过 cls 访问类属性，
静态方法与类和实例无关，只是逻辑上归属该类。
类方法常用于工厂模式，静态方法常用于工具函数。"

# **new** 和 **init** 的区别？

**new** 是对象创建阶段，负责分配内存并返回实例；
**init** 是对象初始化阶段，负责设置属性。
**new** 返回实例后才会调用 **init**，
常用于单例模式、缓存实例、继承不可变类型等场景。

# 什么是魔术方法？

魔术方法是以双下划线包围的特殊方法，Python 在执行特定操作时
自动调用它们，如 **init** 初始化、**add** 实现加法、
**len** 支持 len() 等，是 Python 实现运算符重载
和协议机制的核心。

# 多继承下 MRO 是什么？

MRO 是多继承中方法查找的顺序，Python 3 使用 C3 线性化算法，
保证子类优先、声明顺序一致、单调性。
super() 不是调用父类，而是按 MRO 调用下一个类的方法，
这使得多继承中每个类只被初始化一次

## 生成多继承代码

```python
class A:
    def __init__(self):
        print("A")
        self.a = 10
        super().__init__()
    def say(self):
        print("A say",self.a)
class B:
    def __init__(self):
        print("B")
        self.b = 20
        super().__init__()

    def say(self):
        print("B say",self.b)
class D:
    def __init__(self):
        print("B")
        self.d = 30
    def say(self):
        print("D say",self.d)

class C(A, B, D):
    def __init__(self):
        super().__init__()
        print("C")
    def say(self):
        print("C say",self.a,self.b,self.d)

cc = C()
cc.say()

```

# Python 如何实现单例模式？

## 模块导入

```python
# singleton.py
class _Singleton:
    def __init__(self):
        self.name = "唯一实例"

instance = _Singleton()

# 使用
from singleton import instance   # 模块只加载一次，instance 是全局唯一的
```

## new 重写

有点事方便，缺点是多线程并发下会创建多个实例，线程不安全

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# 测试
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

# 如何实现 LRU 缓存？
