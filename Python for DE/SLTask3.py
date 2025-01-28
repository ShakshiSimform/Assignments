from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

# Test the function for inputs 10, 15, and 20
print("\nOptimized Fibonacci with Memoization:")
print(f"Fibonacci(10): {fibonacci_memoized(10)}")
print(f"Fibonacci(15): {fibonacci_memoized(15)}")
print(f"Fibonacci(20): {fibonacci_memoized(20)}")