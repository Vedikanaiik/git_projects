#2.Input a month(1-12) and enter the number of days in that month using if-elif-else.
# Vedika Naik prn:26070122230

mon= int(input("Enter a month(1-12): "))
if mon ==2:
    print("28 days(29 incase of leap year)")
elif mon in (1, 3, 5, 7, 8, 10, 12):
    print("Month has 31 days")
elif mon in (4, 6, 9, 11):
    print("Month has 30 days")
else: print("Month is Invalid")
