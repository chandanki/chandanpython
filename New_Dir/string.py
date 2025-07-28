i = "abac"
new_str = ""
for r in i:
    new_str =  new_str + (r + "1")
    #new_str += r + "1"
    #print(new_str)
print(new_str)

# i = "*"
'''for i in range(1,10):
    stars = i * '*'
    New_star = "Odd" if i % 2 != 0 else "Even"
    print(f"{stars}  ({New_star})")
    # if i % 2 == 0:
    #     print(stars)'''
stri = "aaeebb"
New_str =""
for i in stri:
    if stri.count(i)>=2:
        New_str = New_str + i + str(stri.count(i))
print(New_str)

string = "eaabbbcdddd"
output = ""
for i in string:
    if i not in output and string.count(i) >= 1:
        output = output + i + str(string.count(i))

print(output)





