friends = {"Tom":"123",'id':'21'}
print(friends)
for i in friends:
    print(i ,':',friends[i])
sorted_keys = sorted(friends.items())
print(sorted_keys)

'''print(friends['Tom'])
friends['bob'] = '543'
print(friends)
del friends["bob"]
print(friends)'''

a = {'a':'chat'}
b = {'b':'bat'}
a.update(b) # to extend dict update function is required
print(a)

# a = ['john','champ','ramp','johny']
# #jnames = [names for names in a if names.startswith('j')]
# jnames = [names for names in a if names[0] == 'j']
# print(jnames)

a = 123
print(str(a)[::-1])

a = ['a','b'] # list with diff ids- 2256142354368
b = ['a','b'] # 2256140941376
print(id(a),id(b))

a = ('a','b') # tupple - with same id - 1936919392832
b = ('a','b') # 1936919392832
print(id(a),id(b))

a = [1,3,5,2]
b = [i for i in a]
b.sort()
print(b)
# swap number by arithmetic
a = 20
b = 30
print(a,b)
a = a + b # 50
b = a - b # 20
a = a - b #30
print(a,b)
