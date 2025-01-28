# List of product dictionaries
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 600},
    {"name": "Monitor", "price": 300}
]

# Use map() to apply a 10% discount to all products
discounted_products = list(map(lambda p: {"name": p["name"], "price": p["price"] * 0.9}, products))

# Use filter() to retrieve products with a price above $500 after discount
expensive_products = list(filter(lambda p: p["price"] > 500, discounted_products))

# Print results
print("Products after applying a 10% discount:")
for product in discounted_products:
    print(product)

print("\nProducts with price above $500 after discount:")
for product in expensive_products:
    print(product)