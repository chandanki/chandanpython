import keyword

print(keyword.kwlist) #print all available keywords in python


['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#  string to list
str = "My name is Chandan"
print(str[-1::-1])
print(list(str))
words = str.split() # split string into list
print(words)
rev = words[::-1] # rev the list
print(rev)
output = "  ".join(rev) # join list into string
print(output)

# while loop to count the length
s = "chandan"
count = 0
while s[count:]:
 count = count+1
 #print(count)
print(count)



