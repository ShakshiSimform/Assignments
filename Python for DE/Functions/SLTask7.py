def analyze_numbers(numbers):
    # map() to square each number
    squared_numbers = map(lambda x: x**2, numbers)
   
    # filter() to keep only numbers greater than 50
    filtered_numbers = filter(lambda x: x > 50, squared_numbers)
   
    # Convert the filtered result to a list and return it
    return list(filtered_numbers)

# Example usage
numbers = [1, 5, 7, 10, 12, 15]
result = analyze_numbers(numbers)
print(result)