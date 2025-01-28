# Task 5: Update the File
with open("students.txt", "r") as file:
    lines = file.readlines()

with open("students.txt", "w") as file:
    for line in lines:
        if line.startswith("Sophie"):
            line = "Sophie, 23, C\n"
        file.write(line)
