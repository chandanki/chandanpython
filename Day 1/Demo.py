from collections import Counter

list = [2,5,6,9,1]
list.sort() # sorting done in ascending order
print("the list",list)
new_list=sorted(list)
print(new_list)


#sorting for decsending order
list = [2,5,6,9,1]
list_1 = sorted(list)
print(list_1)
list.sort(reverse=True)
print(list)

#dictionary
# my_dict = {"name": "Apple", "price": 50,"name1": "ban"}
# sorted_keys = sorted(my_dict.items())
# print(sorted_keys)

#string no. of occurrence
str = "My name is Chandan"
for item in str:
    if str.count(item)>1:
        print(item,str.count(item))
    # print(item,str.count(item)>1)

#list = [1,3,2,4,4,5,5,5]
def duplicate(list):
    for lst in list:
        if list.count(lst)>1:
            print(lst,list.count(lst))

list = [1,3,2,4,4,5,5,5]
print(duplicate(list))
# text = "your profile"
# counts = Counter(text)
# print("count of each char",counts)


    
# my_list = [1, 2, 3, 4, 2, 5, 1]
# unique_list = list(set(my_list))
# print(unique_list)

a = [1,2,5,8,9,4,3,8,8]
b = list[set(a)]
print(b)
# b.sort(reverse =True)
# print(b)
# print(b[1])

