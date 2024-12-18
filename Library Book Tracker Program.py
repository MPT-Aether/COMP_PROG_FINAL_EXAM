def add_book(library):
    title = input("Enter book title: ")
    library.append({"title": title, "borrowed": False})
    print(f"Added '{title}' to the library.")

def view_books(library):
    if not library:
        print("No books in the library.")
    else:
        print("\nLibrary Books:")
        for i, book in enumerate(library, start=1):
            status = "Borrowed" if book["borrowed"] else "Available"
            print(f"{i}. {book['title']} - {status}")

def borrow_book(library):
    view_books(library)
    try:
        book_num = int(input("Enter the book number to borrow: "))
        if not library[book_num - 1]["borrowed"]:
            library[book_num - 1]["borrowed"] = True
            print(f"You borrowed '{library[book_num - 1]['title']}'.")
        else:
            print("This book is already borrowed.")
    except (ValueError, IndexError):
        print("Invalid book number.")

def return_book(library):
    view_books(library)
    try:
        book_num = int(input("Enter the book number to return: "))
        if library[book_num - 1]["borrowed"]:
            library[book_num - 1]["borrowed"] = False
            print(f"You returned '{library[book_num - 1]['title']}'.")
        else:
            print("This book was not borrowed.")
    except (ValueError, IndexError):
        print("Invalid book number.")

def main():
    library = []
    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            view_books(library)
        elif choice == "3":
            borrow_book(library)
        elif choice == "4":
            return_book(library)
        elif choice == "5":
            print("Goodbye have a great day, and remember to return your books!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
