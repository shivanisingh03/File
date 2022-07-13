 
my_file=open("line.txt","r")
count=0
con=my_file.read()
col=con.split("\n")
for i in col:
    count+=1
print("this is the number of line ")
print(count)



my_file=open("line.txt","r")
c=0
for i in my_file:
 c+=1
print(c)




