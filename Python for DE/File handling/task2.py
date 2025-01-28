# Task 2: Read the File
with open("students.txt", "r") as file:
    content = file.read()
    print("File Content:", content)

    lines = content.splitlines()
    print("\nLines:")
    for line in lines:
        print(line)
