class Bar:
    # 멤버 변수(속성) -> 1. 인스턴스 멤버 변수  2. 클래스 멤버 변수
    
    # 클래스 멤버 변수
    # 실무 -> 여기
    
    def __init__(self):
        # 초기화 작업
        # 인스턴스 멤버 변수 : 실무 -> 여기
        pass
    
    def __del__(self):
        # 객체 소멸 전 자원 정리
        pass
    
    # 멤버 메서드 -> 1. 클래스 메서드   2. 인스턴스 메서드
    
    # 인스턴스 멤버 메서드
    def instance_method(self):
        pass
    
    @classmethod
    # 클래스 멤버 메서드
    def class_method(cls):
        pass
    
    
    # static_method
    @staticmethod
    def static_method():
        pass

class Parent:
    def prt_name(self):
        # print(self.name)
        pass

class Child (Parent):
    def __init__(self):
        self.name = "Child"

obj = Child()
obj.prt_name()

class Bar1:
    def __init__(self):
        self.name = "YC Jung"
    
    def prt_info(self):
        # print(self.name, self.age)
        pass

class Foo(Bar1):
    def __init__(self):
        self.age = "18"
        super().__init__()

obj = Foo()
obj.prt_info()