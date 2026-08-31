#Draw a Flowchart and Write a python program to check whether the entered number is prime or not using if -else statement.
#Vedika Naik prn:26070122230
num= int(input("Enter a number: "))

if num<= 1:
    print("The number is not prime.")
else:
    for i in range(2,num):
        if num % i == 0:
            print("The number is not prime.")
            break
    else:
            print("The number is prime.")