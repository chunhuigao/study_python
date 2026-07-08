# 函数的定义
def hello():
    print('hello world')

# 函数的调用
hello()

# 函数的参数
def add_basic(a, b):
    return a + b

# 函数的调用
print(add_basic(1, 2))

# 函数的返回值
def add_return(a, b):
    return a + b

# 函数的调用
print(add_return(1, 2))

# 函数的默认参数
def add_default(a, b=2):
    return a + b

# 函数的调用
print(add_default(1))
print(add_default(1, 3))

# 函数的可变参数
def add_variable(*args):
    total = 0
    for arg in args:
        total += arg
    return total

# 函数的调用
print(add_variable(1, 2, 3, 4, 5))

# 函数的命名空间
def add_namespace():
    a = 10
    b = 20
    print(a + b)

add_namespace()


# 函数的全局变量
def add2():
    global a
    a = 100
    print(a)
add2()
print(a)

# 函数的递归
def add_recursive(a, b):
    if a == 0:
        return b
    else:
        return add_recursive(a - 1, b + 1)
    
# 函数嵌套  
def add_nested(a, b):
    def inner():
        return a + b
    return inner() 

# 函数的调用
print(add_nested(1, 2))

# 函数的闭包
def outer():
    a = 10
    def inner():
        return a
    return inner

# 函数的调用
f = outer()
print(f())
print(f())
print(f())