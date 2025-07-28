'''def sum(start,end):
    result = 0
    for i in range(start,end+1):
        result = result+i
    return result # return result and funct can be call by storing in S variable

s=sum(10,20) # stored in s variable
print(s)'''

# global variable
'''glob = 30
def Fun():
    local =20
    print(glob)
    print(local)
Fun()
print(glob)
print(local) # local variable cant be print because it is define under function , but we can print the global one
good'''
'''t =2
def Glob():
    t =3
    print(t)
    print(t)
    print(globals()['t'])
Glob()'''
# Positional arguments
def Fun(i,j=21):
    print(i,j)
Fun(2) # 2,21
Fun(3,8) # 3,8

# Key word Arguments
def Args(Name,Greeting):
    print(Greeting,"",Name)
Args("chandan","Hi") # Positional Args
Args(Greeting="Hi", Name = "Bhai") # keword Args

# combine keyword vs positional args
def Fun(a,b,c):
    print(a,b,c)
Fun(a=30, b=80,c =5) # Kewword
Fun(6,8,9) # position
Fun(3,c=8,b=5) # cobination of both Key and positional

# (, Separated value return multiple value sin Function and treated as tuple)
def Tup(a,b):
    if a>b:
        return a,b
    elif a==b:
        return a,a
    else:
        return b,a
s=Tup(200,400)
print(s)
print(type(s))




