# Example 1

# class Myclass:  # creating class by giving cass keyword and class name as Myclass
#     def myfun(self):  # deffining method myfun
#         pass
#
#     # def display(self):  #type of instance method which  needs an object
#     #     print("chandan")
#     def display(self,name):
#         print(name)
#
#
# mc1 = Myclass()
# mc1.display("john")
# mc1.myfun()

#Example2

# class Myclass:
#     def m1(self):
#         print("this is instance method")
#     @staticmethod     # this is static method
#     def m2(self,num):
#         print(self,num)
#
# mc=Myclass()
# mc.m1()
# Myclass().m1()
# mc.m2(200,100)
# Myclass.m2(2,3) # static method canbe invoked by direct class name no need to create object

#Example 3

# class Myclass:
#     a,b = 10,20 # class variable
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# mc=Myclass()
# mc.add()
# mc.mul()

#Example4 - Combination of global , class and local variable

# i,j = 10,15
# class Myclass:
#     a,b= 30,20
#     def add(self,x,y):
#         print(x+y)           #local variable
#         print(self.a +self.b) # class variable
#         print(i+j)            # global variable
#
# mc = Myclass()
# mc.add(5,9)

#Example 5 when all variables have same name
# a,b = 10,15
# class Myclass:
#     a,b= 30,20
#     def add(self,a,b):
#         print(a+b)           #local variable
#         print(self.a +self.b) # class variable
#         print(globals()['a'] +globals()['b'])            # global variable
#
# mc = Myclass()
# mc.add(5,9)

#Example 6 : Constructor
#
# class Myclass():
#     def __init__(self):   #default constructor
#         print("this is constructor")
#     def m1(self):
#         print("chandan")
#     def m2(self,x,y):
#         return(x+y)
#
# mc=Myclass() # no need to call function for constructor
# mc.m1()         # need to call function
# print(mc.m2(10,20))

#example7

# class Myclass():
#     name = "caham"
#     def __init__(self,name):  # Parametrised constructor
#         print(name)
#         print(self.name)
#
#
# mc=Myclass("david")

#Example 8 : by display method

# class Myclass:
#
#     def __init__(self,empid,ename,sal):
#
#         self.empid=empid
#         self.ename=ename
#         self.sal=sal
#     def display(self):
#         print(self.empid,self.ename,self.sal)
#
# mc=Myclass(101,"cc bhai",60000)
# #mc.display()
# mc=Myclass(102,"cc bhai",60000)
# mc.display()


#example
class Myclass:

    def __init__(self,empid,ename,sal):

        self.empid=empid
        self.ename=ename
        self.sal=sal
    def __str__(self): # type of constructor which return only string
        return f"Employee ID: {self.empid}, Name: {self.ename}, Salary: {self.sal}"
m1 = Myclass("7766","rr","kkk")
print(m1)