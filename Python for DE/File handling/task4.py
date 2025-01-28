with open("students.txt", 'r') as file:
    lines = file.readlines()

total_students = len(lines) - 1 # Exclude header
grade_a_count = sum("A" in line for line in lines)

print("Total Students:", total_students)
print("Students with Grade 'A':", grade_a_count)
