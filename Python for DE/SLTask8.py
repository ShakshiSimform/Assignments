def custom_aggregate(numbers, func):
    # Initialize the result to the first number (or 0 for sum, 1 for product)
    result = numbers[0] if numbers else 0  # Handle empty list case for sum
    for num in numbers[1:]:
        result = func(result, num)  # Apply the function cumulatively
    return result

# Test with sum lambda function
numbers = [1, 2, 3, 4, 5]
sum_result = custom_aggregate(numbers, lambda x, y: x + y)
print(f"Sum: {sum_result}")

# Test with product lambda function
product_result = custom_aggregate(numbers, lambda x, y: x * y)
print(f"Product: {product_result}")
