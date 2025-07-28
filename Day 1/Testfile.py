import sys

fnames = ['data1.txt', 'data2.png', 'data3.txt', 'view.jpg']
for items in fnames:
    print(items.find('txt'))
    if items[6] == 't': # from index also we can find or endswith for the string
    #if items.endswith('txt'):
        print(items)


# ftext = [files for files in fnames if files.endswith('.txt')]
# print(ftext)

# a = 0o101 # octal number
# b = 3
# print(a+b)
#
# print(sys.version) # to print version of system

'''str = 'welco'
str1 = 'welcome1'
print(id(str), id(str))
print(str.endswith('co')) #True
print(str.startswith("we")) #True
print(str.count("l")) # 1
print(str.find("c")) # 3
print(str.find("d")) #-1
print(str.find("lc")) #2'''

'''a = [1,2,3,4]
print(a)
c = reversed(a)
print(c) # reversed happened but not changed to list , hence list is reuired after reverse
b = list(reversed(a))
print(b)'''
# Checking number s prime or not
'''Num = int(input("Enter number"))
count = 0
if Num >1:
    for num in range(1,Num+1):
        if (Num%num) == 0:
            count = count+1
    if count == 2:
        print("Prime number")
    else:
        print("Not Prime")'''
# Factorial number
'''Num =8
factorial = 1

if Num>= 1:
    for i in range(1,Num+1):
        factorial = factorial * i
    print("factorial is ",factorial)'''

#REcurssive approach
'''n = 1
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print("factorial is", factorial(n))'''

# max from array
# a = [1,3,44,6,44,88]
# #print(max(a))
# max = a[0]
# n =len(a)
# for i in range(1,n):
#     if a[i]>max:
#         max = a[i]
# print("max is", max)

list = [1,2,3,3,4]
count = 0
for i in list:
    count = count+1
print(count)








