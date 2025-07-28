'''list = [1,2,3,6,9,8]
list.sort(reverse=False)# sort() doesnt return any list , its return type is none ( it modifies the list)
print(list)

# using sorted
list = [1,2,3,6,9,8]
c=sorted(list,reverse=True) # it returns new list
print(c)'''

# change list into Set
'''lst =[1,1,2,2,3,3]
my_list = list(set(lst))
print(my_list)'''

# for looop
'''list_2 = [1,2,3,4]
# for i in list_2:
#     print(i, end = '')
list_3 = [i for i in list_2]
print(list_3)'''

'''list = [1,3,2,4,4,5,5,5,6,8]
count = 0
for i in list:
   #print(i, list.count(i))
   #max_count = count+1
   if list.count(i)> 3:
       print(i)
print(list[i])'''
# find items present in list or not
'''a = [1,2,3]
print(6 in a)'''

'''str = "My name is Chandan"
print(str.find("is"))'''
# update list
'''a =[1,3,5]
a[2]=6
a.insert(1,8)
print(a)'''

'''name = "chandan kumar"
for i in name:
    print(i,"=", name.count(i),"times")'''

'''lst = [1, 1,3,3,3,2, 2, 4, 4,5,5]

max_count = 0
most_frequent = None

for i in lst:
    count = lst.count(i)  # Count occurrences of `i`

    if count > max_count:
        max_count = count
        most_frequent = i

print("Most occurring item:", most_frequent)'''

# to fid missing num using sum formula
'''my_list = [1,2,3,5] # for 1 number missing and for multiple then use set
n= len(my_list)+1
s = n*(n+1)//2
sum = sum(my_list)
actual_number = s - sum
print(actual_number) # 4'''
# Set to find multiple number misssing
'''my_list = [1,2,3,4,6,8]
full_set=set(range(1,len(my_list)+2))
set = set(my_list)
print(set)
missing_number = full_set - set
print(missing_number)'''
# for string in list then
'''my_list = ['a','b','c','g','h','k']
full_set = set(chr(i) for i in range(ord(my_list[0]),ord(my_list[-1])+ 1))
missing_num = full_set - set(my_list)
print(missing_num)'''
# for series odd one out
'''my_list = ['abc','bcd','cde','aef']

for word in my_list:

    for i in range(len(word) - 1):
    
        if ord(word[i]) +1 != ord(word[i+1]):
            print(word)
            break'''
str = "Name is one"
for i in str:
    print(i,str.count(i))
print(i)










