x = 100
y = 2.5
z = 4.777766666
a = "welcome"
b = 'abc'
c = True

print(type(x))  # int
print(type(y))  # float
print(type(z))  # float
print(type(a))  # str
print(type(b))  # str
print(type(c))  # bool
print(type(b), type(c))

# write variables in one line instead of multiple lines ---example
a, b, c = 10, 2.5, 'welcome'
print(a, b, c)

# when values of variables are same then -- example
# a = 100
# b= 100
# c = 100
a = b = c = 100
print(a, b, c)

# swapping of two variables --example
x = 1
y = 2
print(x,y) 

y,x = x,y
print( x,y)