# class Student:
    
#     __id_count = 0
    
#     def  __init__(self, name, id, gender):
#         self.name = name
#         self.id = id + Student.__id_count
#         self.gender = gender
#         Student.__id_count += 1
        
#         self.grade_korean = 0
#         self.grade_math = 0
#         self.grade_english = 0
#         self.total = 0
#         self.avg = 0

#     def set_score(self, korean, math, eng):
#         self.grade_korean = korean
#         self.grade_math = math
#         self.grade_eng = eng
#         self.grade_total = korean + math + eng
#         self.avg = self.total / 3
    
#     def get_total_avg(self):
#         return (self.total, self.avg)

#     @classmethod
#     def get_id_count(cls):
#         return cls.__id_count
    
#     @staticmethod
#     def get_avg(arg1, arg2, arg3):
#         return (arg1 + arg2 + arg3) / 3

# class Car:
    
#     __car_count = 0
    
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.id = Car.__car_count
#         Car.__car_count += 1
        
#         self.mileage = 0
#         self.fuel = 0
    
#     def drive(self, distance):
#         self.mileage += distance
#         self.fuel -= distance * 0.1
    
#     def refuel(self, amount):
#         self.fuel += amount
    
#     @classmethod
#     def get_car_count(cls):
#         return cls.__car_count
    
#     @staticmethod
#     def calculate_mileage(distance, fuel_used):
#         return distance / fuel_used


# class Vehicle():
    
#     __vehicle_count = 0
    
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         Vehicle.__vehicle_count += 1
        
#         self.mileage = 0
    
#     def drive(self, distance):
#         self.mileage += distance
        
#     @classmethod
#     def get_vehicle_count(cls):
#         return cls.__vehicle_count
    
    

# class Car(Vehicle):
#     def __init__(self, brand, model, year):
#         super().__init__(brand, model, year)
        
#         self.fuel = 0
    
#     def drive(self, distance):
#         self.fuel -= distance * 0.1
#         self.millage += distance
    
#     def refuel(self, amount):
#         self.fuel += amount

# class ElectricCar(Vehicle):
#     def __init__(self, brand, model, year):
#         super().__init__(brand, model, year)
        
#         self.battery = 100
    
#     def drive(self, distance):
#         self.battery -= distance * 0.2
#         self.mileage += distance
    
#     @staticmethod
#     def battery_efficiency(distance, battery_used):
#         return distance / battery_used


from abc import ABC, abstractmethod

class Shape(ABC):
    
    __shape_count = 0
    
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
        Shape.__shape_count += 1
    
    @property
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    @classmethod
    def get_shape_count(cls):
        return cls.__shape_count
    
    @staticmethod
    def is_color_valid(color):
        if (color):
            return True
        else:
            return False

class Circle(Shape):
    
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.__radius = radius
        self.__area = 3.14 * radius ** 2
    
    @property
    def area(self):
        return self.__area

    def perimeter(self):
        return self.__radius * 2 * 3.14