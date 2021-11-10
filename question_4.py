my_file=open("question_4.txt","r")
for i in my_file:
    if "delhi" in i:
        my_file1=open("delhi.txt","a")
        my_file1.write(i)
    elif "shimla" in i:
        my_file2=open("shimla.txt","a")
        my_file2.write(i)
    else:
        my_file3=open("other.txt","a")
        my_file3.write(i)

