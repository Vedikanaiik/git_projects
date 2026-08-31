#Accept a number and check whether it is divisible by both 5 and 11, only by 5, only by 11, or not divisible using nested-if .
#Vedika Naik prn:26070122230
a= int(input("Enter a number: "))
if a % 5 == 0:
    if a % 11 == 0:
        print("Divisible by both 5 and 11")
    else:
        print("Divisible by 5 but not by 11")
else:
    if a % 11 == 0:
        print("Divisible by 11 but not by 5")
    else:
        print("Not divisible by 5 or 11")
    
        