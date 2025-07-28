class MyClass:
    def display(self): # self is a keyword which says this function(display) belongs to MyClass
        print("selected")
    def display_1(self,name):
        print("name is",name)
mc=MyClass() # object created means memory allocated
mc.display()
mc.display_1("John")

# Instance method (through object i can call method)
# Static method () in Python there is no any static variable like java, but static method only
'''class MyClass:
    def m1(self):
        print("instance method")

    @staticmethod # this not belongs to class , so no need to create object
    def m2(self): # here we can pass self or not , depends upon user
        print(self)
MyClass.m2("self")# No need to create object , we can call method by Classname
mc = MyClass()
mc.m2(11) # we can also call it by creating class object but it would be more useful if we call it by class name
mc.m1()'''

# declaring class variable
'''i,j = 20,45 # Global variable ( outside of the class)
class Hello:
    a,b,c = 10,20,30 # Class variable
    def m1(self,x,y): # local variable (within method)
        print(self.a+self.b+self.c) # class variable define by self.a and self.c
        print(x+y)
        print(i+j)
obj1=Hello()
obj1.m1(11,21)'''

# if all class , global, local variables has same name then
'''a, b = 22,91 # Global variable
class Hi:
    a,b = 1,2
    def add(self,a,b): # local variable
        print(a+b)
        print(self.a+self.b) # self kw used for class variable
        print(globals()['a']+globals()['b']) # global keyword used for global variable
obj=Hi() # Named object (obj name given to Hi class reference)
obj.add(17,4)
Hi().add(1,7) # Nameless object ( No name given to the object)
print(id(obj.add(1,4)))
print(id(obj))
obj1 = Hi()
print(id(obj1))'''

# Constructor
'''class Hello(): # class Hello: - Both are correct
    def add(self):
        print("addition done")
    def __init__(self):
        print("this is constructor")
obj=Hello()
obj.add()
#Hello().__init__() #-Nameless object'''

# Convert local variable into class variable
'''class Feb:
    def m1(self,a,b):
        print("value",a+b) # local variable
        self.a = a  # here a is local variable and self.a is class variable
        self.b = b
        self.add()
    def add(self):
        print(self.a+self.b) # class variable
obj=Feb()
obj.m1(1,3)
# obj.add()'''

#Call 1 method and this method call another method within class
'''class Nov:
    def m1(self):
        print("method 1") 
        self.m2(1) # here we call m2() by m1() only
    def m2(self,a):
        print("method 2")
obj=Nov()
obj.m1() # only m1() called'''

#__str__ constructor
'''class Tool:
    # pass
    def __str__(self):
        return "welcome"
obj=Tool()
print(obj)

# __del__ constructor
class Cool:
    def __del__(self):
        print("destroyed")
c1 = Cool()
c2 = Cool()
#print(c1)'''

class M:
    @classmethod
    def add(self):
        print("this is class method")
M.add()



