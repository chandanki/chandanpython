# ABC predefined for abstract class
from abc import ABC, abstractmethod


# class A(ABC):
#     @abstractmethod
#     def display(self):
#         print("This is from A")
#     @abstractmethod
#     def eat(self):
#         print("This is from C")
#
#
# class B(A):
#     def display(self):
#         print("this is from B")
#
# class C(B):
#     def eat(self):
#         print("This is from C")
#
# obj = C()
# obj.display(),obj.eat()

# for constructor
class A(ABC):
    def __init__(self,a,b): # this is local variable of method only not for class
        self.a = a    # Now this is class variable
        self.b = b

    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
class B(A):
    def add(self):
        print(self.a+10)
    def sub(self):
        print(self.b-2)

obj=B(11,12)
obj.add()
obj.sub()