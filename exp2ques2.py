#q2. Grocery Billing System
# Name: Vedika Pradeep Naik
#prn: 26070122230 cse c-3
store = {
    "Eggs()": 20,
    "Rice(kg)": 110,
    "Wheat(kg)": 113,
    "Salt(1kg/packet)": 25,
    "Sugar(1kg/packet)": 25
}

bill = []

item = input("\nEnter item name: ")
quantity = int(input("Enter quantity: "))

if item in store:

    if quantity <= store[item]:

        price = float(input("Enter price per unit: "))

        bill.append((item, quantity, price))

        store[item] = store[item] - quantity

        print("Item added to bill.")

    else:
        print("Not enough stock available.")

else:
    print("Item not available.")


print("\nReceipt:")
total = 0

for item, quantity, price in bill:
    amount = quantity * price
    print(item, quantity,"x", price, "=", amount)

    total = total + amount

print("Total Bill =", total)