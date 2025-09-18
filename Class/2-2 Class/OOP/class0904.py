class Foo:
    name = "Class member variable: Foo" # 클레스 멤버 변수
    # 멤버메서드
    def test(instance_ref):
        # 인스턴스 멤버변수
        instance_ref.name = "Instance member variable: Foo"
        

obj = Foo()
obj.test()

print(obj.name)

class Foo2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def set_name(self, name):
        self.name = name
    
    def set_age(age):
        pass

obj = Foo2()

obj.university = "YJU"
print(obj.university)


# obj.set_name("Hong")    # -> Foo.set_name(obj, "Hong")
# print(obj.name)

# del obj.set_name
# obj.set_name("Kim")

# del obj.name
# print(obj.name)