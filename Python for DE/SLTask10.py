def dynamic_function(numbers, operation):
    if not numbers:  # Handle empty list case
        return None

    # Define operations using lambda functions
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else float("inf"),  # Handle division by zero
    }

    # Check if the operation is valid
    if operation not in operations:
        raise ValueError(f"Invalid operation: {operation}")

    # Dynamically apply the operation
    result = numbers[0]
    for num in numbers[1:]:
        result = operations[operation](result, num)

    return result

# Testing the function
numbers1 = [10, 5, 2]
numbers2 = [1, 2, 3, 4]

print(f"Add: {dynamic_function(numbers1, 'add')}")        
print(f"Subtract: {dynamic_function(numbers1, 'subtract')}")  
print(f"Multiply: {dynamic_function(numbers2, 'multiply')}")  
print(f"Divide: {dynamic_function(numbers1, 'divide')}")      