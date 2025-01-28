# Task 8: Word Count
# Create the file
with open("paragraph.txt", "w") as file:
    file.write("This is a sample paragraph only. This paragraph is written for testing purposes.Not to use this paragraph anywhere else.")

# Word count
with open("paragraph.txt", "r") as file:
    content = file.read()
    words = content.split()
    word_count = len(words)

    search_word = input("Enter a word to count its occurrences: ").strip()
    word_occurrences = words.count(search_word)

print("Total Words:", word_count)
print(f"Occurrences of '{search_word}':", word_occurrences)
