'''print("exception handling")
print("exception handling")

try:
    print(x)
except:
    print("client side error")

print("exception handling successful")
print("exception handling successful")'''

print("except block")
try:
    #print(10/2)
    print(10/0)
except :
    print("handled exception")
else:
    print("no exception")
finally:
    print("final block")

print("programming done")