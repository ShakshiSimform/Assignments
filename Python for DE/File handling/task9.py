# Task 9: Copy File Content
with open("students.txt") as source, open("students_backup.txt", "w") as dest:
    for line in source:
        dest.write(line)
