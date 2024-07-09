global_var=20

def fun():
    local_var=10
    print(local_var)
    print(global_var)
fun()
#print(local_var)---this is invalid becoz calling function outside
print(global_var)