#Write a python program to display the menu of a calculator and perform addition, subtraction ,multiplication and division based on user choice.
# Vedika Naik prn: 26070122230
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation=input("Enter operation to be performed: ")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if  operation == "Addition":
    print("Addition = ", num1 + num2)

elif operation == "Subtraction":
    print("Subtraction =", num1 - num2)

elif operation == "Multiplication":
    print("Multiplication =", num1 * num2)

elif operation == "Division":
    print("Division =", num1 / num2)

else:
    print("Invalid choice")