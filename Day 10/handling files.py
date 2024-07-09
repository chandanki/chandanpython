#Example 1 : writing data into text file
# file = open("C:\Demofiles\open.txt",'w')
# file.write("this is first line\n")
# file.write("this is second line\n")
# file.write("this is third line")
# file.close()
# print("programme done")

# Example 2 : reading data from text file

# file = open("C:\Demofiles\open.txt",'r')
# print(file.read())
# file.close()

#example 3 : append data in txt
file = open("C:\Demofiles\open.txt",'a')
file.write("\nthis is one\n")
file.write("this is two")
file.close()