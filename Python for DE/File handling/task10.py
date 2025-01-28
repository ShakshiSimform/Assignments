# Task 10: Delete a File
import os

if os.path.exists("students_backup.txt"):
    confirm = input("Do you want to delete students_backup.txt? (yes/no): ").strip().lower()
    if confirm == "yes":
        os.remove("students_backup.txt")
        print("File deleted.")
    else:
        print("File not deleted.")
else:
    print("File does not exist.")
