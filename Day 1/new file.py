print("hello world : I am ready for my python")

# for printing x+y
x = 100
y = 20
print(x+y)


'''def fetch_data():
    connection = mysql.connector.connect()
    if connection.is_connected():
        print("connection is secure ")

        cursor = connection.cursor()
        query = "SELECT * from table"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Fetched data from table")
        for row in rows:
            print(row)'''

string = "Test Framework"

for item in string:
    if string.count(item) <= 1:
        print (item)

# swap 1st and last number
a =[1,4,7,9,8]
'''size = len(a)
temp = a[0]
a[0] = a[size-1]
a[size-1] = temp'''
a[1],a[2] = a[2],a[1]
print("mylist",a)

a =[1,4,7,9,8,4]
ele = 100
'''flag =0
for i in a:
    if(i==ele):
        print("element found")
        flag =1
        break
if (flag ==0):
        print("element not found")'''
if (ele in a):
    print("found")
else:
    print("Not found")
b=[1,3,4,5,6,9,4,9,8,9]
x = 9
count = 0
for i in b:
    if (i==x):
        count = count+1
print("{} occured {} times".format(x,count))
b=[1,3,4,5,6,9,4,9,8,9]
print(max(b))
c=set(b)
print(c)
print(max(c))

# pallindrome number
s = "maaam"
rev =s[::-1]
if rev == s:
    print("pallindrome")
else:
    print("Not pallindrome")

# for number pallindrome or not
s = [4,5,2,2]
str=sum(s)
print(str)
rev = s[::-1]
revstr = sum(rev) # sum is not consider for pallindrome only reverse of it consider
if str == revstr:
    print("pallindrome")
else:
    print("Not pallindrome")





