# class Myclass:
#     __a = 10  # Private variable
#     b= 20  # Public varible
#
#     def disp(self):
#         print(self.__a)
#
# obj = Myclass()
# obj.disp()
#
# print(Myclass.b)
# print(Myclass.__a) # we can not access variable "a", bcoz it is private one

#Now for private method
# class myclass:
#     def __disp1(self): # Private method
#         print("this is method 1")
#
#     def disp2(self):
#         print("this is method 2")
#         self.__disp1()
#
# obj = myclass()
# #obj.__disp1() # it is wrong
# obj.disp2()

# Aceess private variable outside of class by methods
class myclass():
    __id1 = 10

    def get(self,id2):
        self.__id1 = id2
        print(self.__id1)

    def dispid(self):
        print(self.__id1)

obj = myclass()
obj.get(11)
obj.dispid()