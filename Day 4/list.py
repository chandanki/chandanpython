# mylist= ["orange","banana","apple","chiku"]
# # print(mylist)
# # mylist.pop(0)
# # print(mylist)
# # # mylist.clear()
# # #print(mylist)
#
# name = "chandan kumar"
# for i in name:
#     print(i,"=", name.count(i),"times")
#
# list = [1,2,3,3,4,6,6,5]

list1 = list("Python")
print(list1)

# l= [1,2,3]
# print(l[0])
# print(2 in l)
# print(2 not in l)
# print(len(l))
# for i in l:
#     print(i)

a = 10
b = 20
print(a,b) # 10, 20
a , b = b, a
print(a,b) # 20,10

# print in one line then
# list_2 = [1,2,3,4]
# for i in list_2:
#     print(i, end = '')

list_3 = [x+2 for x in range(10)]
print(list_3)

'''for x in range(10):
    if(x% 2 != 0):
        print(x,end = ' ')'''
list_4 = [x for x in range(10) if x% 2 ==0]
print(list_4)
