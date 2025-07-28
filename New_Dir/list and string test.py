'''my_list = ["a","b","c"] # print only a and c
n = len(my_list)
print(n)
for i in range(1,n,2):
    print(my_list[i],end=' ')'''

# reverse string
'''n_list = [1,2,3,4]
r_list=[]
n = len(n_list)
for i in n_list[::-1]:
    r_list.append(i)
print(r_list)'''

'''str = "My Name"
rev_str = ""
for i in str:
    rev_str =  (i+"1") + rev_str
print(rev_str)'''

str = "my name is Chandan Kumar"
for i in str:
    print(i,str.find(i))
rev_str = str.split()
print(rev_str)
n = len(rev_str)
for i in range(n):
    if (i + 1) % 2 == 0:
        new_str = rev_str[::-1]
    else:
        rev_str[i] = rev_str[i][::-1]

print(rev_str)
output = " ".join(rev_str)
print(output)
s_str = " ".join(new_str)
print(new_str)
print(s_str)