#*args for passing arguments , it can be denoted as *a or *b

def sum(*args):
    s = 0
    for i in args:
        s+= i # s= s+i
    print("sum is",s)
sum(3,2,1)

# send args to function
def arg(a,b,c):
    print(a,b,c)

li= [1,2,3]   #list
arg(*li)

# **kargs , ** represents for key and value like 'name'= "chandan"
def arg(a,b,c):
    print(a,b,c)
a= {"a":"one","b":"two","c":"vv"}
arg(**a)

# example2 for kwargs
def my_fun(**kargs):
    for i,j in kargs.items():
        print(i,j)
my_fun(name= "tom",sport= "ran",team="India")


