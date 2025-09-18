class Bar:
    
    # Constructor
    def __init__(self, id):
        # Add instance member variables
        self.id = id
        print(f"Constructor of object {self.id} is invoked")
    
    def __del__(self):
        print(f"Destructor of object {self.id} is invoked")
    
    # # instance method
    # def i_method(self):
    #     self.iValue = 20
        
    # # class method
    # @classmethod
    # def c_method(cls):
    #     cls.cValue = 30
            
obj1 = Bar(1)
obj2 = Bar(2)
del obj1
print("Program is terminated")
del obj2