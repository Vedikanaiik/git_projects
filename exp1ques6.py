#Generate the Fibonacci sequence up to n terms using a while loop.
#Vedika Naik prn: 26070122230

n= int(input("Enter number of terms: "))
i, j = 0, 1
count= 0
while n > count:
    print(i, end=", ")
    next_term = i + j
    i=j
    j= next_term
    count += 1