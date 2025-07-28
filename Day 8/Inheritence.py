# example 1 ( single Inheritence)

# class A:
#     def m1(self):  #method only not variable
#         print("this is class A")
#
# class B(A):
#     def m2(self):
#         print("this is class B")
#
# bobj = B()
# bobj.m1()
# bobj.m2()

#example 2
class A:
    x,y = 10,20      #variable and method
    def m1(self):      #method
        print(self.x,self.y)

class B(A):
    a,b = 20,70
    def m2(self):
        print(self.a-self.b)

bobj = B()
bobj.m1()
bobj.m2()

#Example 3 (Multilevel Inheritence)
# class A:
#     x,y = 10,20      #variable and method
#     def m1(self):      #method
#         print(self.x,self.y)
#
# class B(A):
#     a,b = 20,70
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j= 12,13
#     def m3(self):
#         print(self.i,self.j)
#
# bobj = C()
# bobj.m1()
# bobj.m2()
# bobj.m3()

#example 4 (Hierarchy Inheritance)
# class A:
#     x,y = 10,20      #variable and method
#     def m1(self):      #method
#         print(self.x,self.y)
#
# class B(A):
#     a,b = 20,70
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j= 12,13
#     def m3(self):
#         print(self.i,self.j)
#
# bobj = B()
# bobj.m1()
# bobj.m2()
# bobj = C()
# bobj.m1()
# bobj.m3()

# #Example 5
# class A:
#     x,y = 10,20      #variable and method
#     def m1(self):      #method
#         print(self.x,self.y)
#
# class B:
#     a,b = 20,70
#     def m2(self):
#         print(self.a-self.b)

# class C(A,B):
#     i,j= 12,13
#     def m3(self):
#         print(self.i,self.j)
#
# bobj = C()
# bobj.m1()
# bobj.m2()
# bobj.m3()

# Example : Method Overriding
#
class A:
    def m1(self):
        print("m1 from classA")
class B(A):
    def m1 (self):
        print("m1 from class B")
        super().m1()  #this calls the parent class method

bobj = B()
bobj.m1() # call the latest implementation

#Example : Overiding variable

class Parent:
    name = "john"
class Child(Parent):
    name = "chandan"
    def test(self):
        print(super().name)

obj= Child()
print(obj.name)
obj.test()

#example 1 overloading
# class Over:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
#     # def add(self,i=0,j=0,k=0): # used in java
#     #     print(i+j+k)
#
# obj= Over()
# obj.add()
# obj.add(10,20)
# obj.add(10,20,30)
# obj.add(23,45,55)
# obj.add(66,77)

#example2

class Name:
    def hello(self,name=None):
        if name is not None:
            print("hello"+ name)
        else:
            print("hi")

h= Name()
h.hello("World")
h.hello( )

#Example of module
def add(a,b):
    print(a+b)

add(10,20)


