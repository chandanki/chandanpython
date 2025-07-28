list = [1,2,5,5,4,5,5,5,6,6,6,6,6,]
max_count = 0
n = len(list)
max = list[0]
for i in range(n):
    count = 0
    for j in range(n):
        if list[i] == list[j]:
            count += 1
if count > max_count:
    max = list[i]
print(max)