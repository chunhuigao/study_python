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
