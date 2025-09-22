menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80,
}

print("Welcome to PYTHON Restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs{price}")

order_total = 0

item_1 = input("Enter the name of the item you want to order: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available yet!")

another_order = input("Do you want to order another item? (yes/no): ").lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available yet!")

print(f"The total amount to pay is: Rs{order_total}")
