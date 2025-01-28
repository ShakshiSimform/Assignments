# Task 6: Create and Work with Large Files
with open("numbers.txt", "w") as file:
    file.writelines(f"{i}\n" for i in range(1, 1001))

with open("numbers.txt") as file:
    total_sum = sum(map(int, file))
print("Sum of Numbers:", total_sum)
