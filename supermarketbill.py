# Supermarket Billing System

user_name = input("Can you share your good name: ")
print(f"Hello {user_name}, welcome to our SUPERMART!")

print("\nHere is the list of items available:\n")

items = {
    'rice': 20,
    'sugar': 30,
    'salt': 20,
    'oil': 80,
    'paneer': 110,
    'maggie': 50,
    'boost': 90,
    'colgate': 85
}

print("Item\t\tPrice (per unit)")
print("-" * 30)
for item, price in items.items():
    print(f"{item.capitalize():<10}\t₹ {price}/kg")

cart = []
total = 0

while True:
    choice = input("\nDo you want to add an item to your cart? (yes/no): ").lower()
    if choice == 'no':
        break
    elif choice == 'yes':
        item = input("Enter item name: ").lower()
        if item in items:
            qty = int(input(f"Enter quantity (in kg/units) for {item}: "))
            price = items[item] * qty
            cart.append([item, qty, items[item], price])
        else:
            print("Sorry, that item is not available.")
    else:
        print("Please enter 'yes' or 'no'")

if cart:
    print("\n" + "=" * 50)
    print("SUPERMART FINAL BILL".center(50))
    print("=" * 50)
    print(f"{'Item':<12}{'Qty':<8}{'Rate':<10}{'Total':<10}")
    print("-" * 50)

    for item, qty, rate, price in cart:
        print(f"{item.capitalize():<12}{qty:<8}{rate:<10}{price:<10}")
        total += price

    gst = round((total * 5) / 100, 2)
    grand_total = total + gst

    print("-" * 50)
    print(f"{'Subtotal':<30} ₹ {total}")
    print(f"{'GST (5%)':<30} ₹ {gst}")
    print(f"{'Grand Total':<30} ₹ {grand_total}")
    print("=" * 50)
    print("Thank you for shopping with us!".center(50))
else:
    print("\nYour cart is empty. No bill generated.")
