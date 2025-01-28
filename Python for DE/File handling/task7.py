# Task 7: Error Handling
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)
