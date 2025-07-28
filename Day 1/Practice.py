a = [6,7,8,500]
# max = max(a)
# print(max)
'''n = len(a)
max = a[0]
for i in range(0,n):
    if a[i]>max:
        max_num = a[i]
print("Max number",max_num)'''
print(a)
a[0],a[3] = a[3],a[0] # a,b = b,a
print(a)

'''count = 0
for i in a:
    count = count + 1

print(count)'''

a = [8,3,6,7]
n = len(a)
# for i in range(1,n):
#     a[i]= (a[i]+3)- 2
# print(a)
# for i in range(0,n):
#     a[i]= (a[i]+3)- 2
# print(a)
i = 1
while i<n:
    a[i]= a[i]+1
    #i = i+1
    i+= 1
print(a)





