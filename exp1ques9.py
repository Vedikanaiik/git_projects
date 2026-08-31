#9.Display the multiplication tables from 5 to 10 using nested for loops.
# Vedika Naik prn:26070122230
print(" Multiplication tables 5-10")

for num1 in range(5, 11):
    for num2 in range(1, 11):

        print(num1, "x", num2, "=", num1 * num2, end="\n")
    print()

