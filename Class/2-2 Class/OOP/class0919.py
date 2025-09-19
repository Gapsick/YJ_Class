class A:
    def prt(self):
        print("A - prt")

class B(A):
    pass
    # def prt(self):
    #     print("B - prt")

class C(A):
    pass
    # def prt(self):
    #     print("C - prt")
    
    
class D(B, C):
    def __init__(self):
        print("D")

# obj = D()
# obj.prt()

# Over Riding
class Parent:
    def prt(self):
        print("Parent")

class Child(Parent):
    pass
    # def prt(self):
    #     print("Child")

obj = Child()
obj.prt()  # Child


