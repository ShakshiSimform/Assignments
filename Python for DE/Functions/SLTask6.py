import time

# Optimized decorator to calculate execution time
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # High precision timer
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.perf_counter()  # High precision timer
        print(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds")
        return result  # Return the result of the original function
    return wrapper

# Optimized factorial function (iterative version for large numbers)
@execution_time
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test the optimized decorator with a large number (e.g., 1000)
print("Factorial of 1000:")
factorial(1000)
