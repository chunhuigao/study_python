class ClassName:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + b
        print(self.c)

numberAdd = ClassName(1, 2)
print(numberAdd.a)
print(numberAdd.b)
print(numberAdd.c)

# 类的调用
print(numberAdd.c)

# 类的方法  
def add(self):
    return self.a + self.b

# 类的属性
print(numberAdd.a)
print(numberAdd.b)
print(numberAdd.c)

# 类继承
class ClassName2(ClassName):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.d = a * b
        print(self.d)
print(ClassName2(10, 2).d)
