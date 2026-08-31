#Input percentage and print remarks: Excellent / Very Good / Good / Average / Fail.
# Vedika Naik prn: 26070122230
score= int(input("Enter your Percantage: "))
if score<= 40:
    print("Fail")
elif score>= 40 and score<= 59:
    print("Average")
elif score>= 60 and score<= 74:
    print("Good")
elif score>= 75 and score<= 89:
    print(" Very Good")
elif score>90:
    print("Excellent")
else: print("Marks are invalid")