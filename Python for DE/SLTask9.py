data = [
    {"name": "Alice", "age": 30, "score": 85},
    {"name": "Bob", "age": 25, "score": 90},
    {"name": "Charlie", "age": 35, "score": 95}
]

# Extract the names of all individuals
names = list(map(lambda p: p["name"], data))
print(f"Names: {names}")

# Calculate the average score of all individuals
average_score = sum(map(lambda p: p["score"], data)) / len(data)
print(f"Average Score: {average_score}")
