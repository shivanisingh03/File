# Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam ki
#  file mein nayi line mein daalo. Aapki list yeh rahi:

# my_file=open("file-question3.txt")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
my_file=open("file-question3.txt","w")
i=0
while i<len(banks_list):
    my_file.write(banks_list[i])
    my_file.write("\n")
    i=i+1

