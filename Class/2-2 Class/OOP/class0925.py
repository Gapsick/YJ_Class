class A:
    def __init__(self):
            self.public = "public"
            self.protected = "protected"
            self.__private = "private"
            # self.class name__variable name

class B(A):
    def print(self):
        print(self.public)
        print(self._protected)
        print(self._A__private)
        

obj = B()
# obj.prints()