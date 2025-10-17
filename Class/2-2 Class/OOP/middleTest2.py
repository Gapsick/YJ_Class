# class Student:
#     __id_count = 0
    
#     def __init__(self, name, id, gender):
#         self.name = name
#         self.id = Student.__id_count
#         self.gender = gender

#         self.grade_korean = 0
#         self.grade_math = 0
#         self.grade_english = 0
#         self.total = 0
#         self.avg = 0
        
#         Student.__id_count += 1

#     def set_score(self, korean, math, eng):
#         self.grade_korean = korean
#         self.grade_math = math
#         self.grade_english = eng
        
#         self.total = korean + math + eng
#         self.avg = self.total / 3
    
#     def get_total_avg(self):
#         return (self.total, self.avg)
    
#     @classmethod
#     def get_id_count(cls):
#         return cls.__id_count
    
#     @staticmethod
#     def get_avg(arg1, arg2, arg3):
#         return (arg1 + arg2 + arg3) / 3
    
    

# s1 = Student("Alice", 0, "F")
# s2 = Student("Bob", 0, "M")

# s1.set_score(90, 85, 92)
# s2.set_score(75, 80, 78)

# print(s1.get_total_avg())
# print(s2.get_total_avg())

# print(Student.get_id_count())
# print(Student.get_avg(100, 90, 80))

from abc import ABC, abstractmethod


class Animal(ABC):
    
    count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count += 1
    
    @abstractmethod
    def sound(self):
        pass

    def prt_info(self):
        return self.name, self.age
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @staticmethod
    def is_animal(obj):
        if (obj.isinstance(obj, Animal)):
            return True
        else:
            return False

class Dog(Animal):
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def sound(self):
        print("멍멍")

class Cat(Animal):
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def sound(self):
        print("야옹")

class GuideDog(Dog):
    
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner
