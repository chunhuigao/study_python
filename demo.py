
## 生成多继承代码

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
    

