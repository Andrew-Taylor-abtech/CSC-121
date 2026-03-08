sandwich_orders = ["italian grinder", "tuna", "meatball sub", "all veggie"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print("I made your " + current_sandwich.title() + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches are made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())  