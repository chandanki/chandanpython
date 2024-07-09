# ways of creating string variables
# s = 'welcome'
# s = str("welcome")

x = 12
print(id(x))

# mutable - cannot change the value
# Immutable - Can change the value
# string is immutable

# Example 1:
# + and * operators with the string
# str = 'welcome'
# print(str + "python")  # joining/Concatenation
# print("python"*3)    # printing 3 times

#example 2 : slicing[]
# starting index should 0
# but ending index counts as 1 or (n-1)

str = "welcome"
# print(str[1:3])  #el
# print(str[:5])   #bydefault it takes as 0 for starting index
# print(str[2:])   # consider all after starting index
# print(str[1:-4])   # deduct last 4 characters from string
print(str[-2:3])

#example 3: get ord() and chr() ascii value
# print(ord('B'))  #66
# print(chr(66))   #B
# print(ord('&'))

#max() , min(), Len() function
# print(max('abc'))  #c
# print(min('abc'))  #a
# print(len("123"))  #3

#example 4: in notin operators
# s="welcome"
# print("ome" in s)
# print("lc"in s)
# print("cc" in s)
# print("cc" not in s)

#string comparision
# print("tim" == "team")
# print("tim" == "tim")
# print("tim" != "yim")
# print("red"> "bed")
# print("ted" <= "ced")

# print("first".isidentifier())
# print("welcome" .isnumeric())
# print("welcome to delhi".find("uu"))
# print("welcome to delhi".count("hi"))

#reverse string(Example)

# s = "radhe"
# reverse_s =""
# for i in s:
#     reverse_s = i + reverse_s
#
# print("reversed string is:", reverse_s)

#method 2 for reverse string
s = "radhe"
rev_s = s[::-1]
print(rev_s)


