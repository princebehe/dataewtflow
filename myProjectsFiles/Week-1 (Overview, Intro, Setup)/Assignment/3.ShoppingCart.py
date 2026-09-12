cart = {}

print("Welcome to the Shopping Cart! (Type 'done' when finished)")
while True:
    item_name = input("Enter item name: ").strip()
    if item_name.lower() == 'done':
        break
    try:
        item_price = float(input(f"Enter price for {item_name}: "))
        cart[item_name] = item_price
    except ValueError:
        print("Please enter a valid number for the price.")

# Display items and total cost
print("\n--- Your Shopping Cart ---")
total_cost = 0
for item, price in cart.items():
    print(f"{item}: ${price:.2f}")
    total_cost += price

print(f"Total Cost: ${total_cost:.2f}")