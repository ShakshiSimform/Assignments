def apply_discount(price, discount_function):
    discounted_price = discount_function(price)
    return discounted_price

# Discount strategies as lambda functions
flat_discount = lambda price: price - 50  # Flat $50 discount
percentage_discount = lambda price: price * 0.8  # 20% discount

# Test the apply_discount function with both strategies
original_price = 250

# Test with flat discount
discounted_price_flat = apply_discount(original_price, flat_discount)
print(f"Original price: ${original_price}, Price after flat discount: ${discounted_price_flat}")

# Test with percentage discount
discounted_price_percentage = apply_discount(original_price, percentage_discount)
print(f"Original price: ${original_price}, Price after 20% discount: ${discounted_price_percentage}")