# a = 5
# b = 10
#
# temp = a
# a = b
# b = temp
# print ("after swap",a,b)
from collections import Counter

# count char

text = "helloooo"
# count = text.count('o')
# print(f"o times{count}")
counts = Counter(text)
print("count of each char",counts)
