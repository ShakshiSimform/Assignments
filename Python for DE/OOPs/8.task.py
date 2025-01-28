class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"You borrowed {book}")
        else:
            print(f"{book} is not available.")

    def return_book(self, book):
        self.books.append(book)
        print(f"You returned {book}")

# Create Library object and interact
library = Library(["Python Programming", "Data Structures", "Algorithms"])

while True:
    print("\n1. Display Books\n2. Borrow Book\n3. Return Book\n4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        library.display_books()
    elif choice == 2:
        book = input("Enter the book name to borrow: ")
        library.borrow_book(book)
    elif choice == 3:
        book = input("Enter the book name to return: ")
        library.return_book(book)
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
