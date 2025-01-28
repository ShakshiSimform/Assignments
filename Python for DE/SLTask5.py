# List of product dictionaries
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 600},
    {"name": "Monitor", "price": 300}
]

# Sort products by price in ascending order
products_sorted_ascending = sorted(products, key=lambda p: p["price"])

# Sort products by price in descending order
products_sorted_descending = sorted(products, key=lambda p: p["price"], reverse=True)

# Print results
print("Products sorted by price (Ascending):")
for product in products_sorted_ascending:
    print(product)

print("\nProducts sorted by price (Descending):")
for product in products_sorted_descending:
    print(product)