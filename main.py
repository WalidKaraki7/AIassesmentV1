from library.book_manager import BookManager

def print_menu():
    print("\nLibrary Management System")
    print("1. List all books")
    print("2. Add a book")
    print("3. Edit a book")
    print("4. Delete a book")
    print("5. Search books by title")
    print("6. Search books by author")
    print("0. Exit")

def main():
    manager = BookManager()
    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            books = manager.list_books()
            for book in books:
                print(f"{book['id']}: {book['title']} by {book['author']}")
        elif choice == "2":
            title = input("Enter title: ")
            author = input("Enter author: ")
            book = manager.add_book(title, author)
            print(f"Added: {book}")
        elif choice == "3":
            book_id = int(input("Enter book ID to edit: "))
            title = input("New title (leave blank to keep): ")
            author = input("New author (leave blank to keep): ")
            book = manager.edit_book(book_id, title or None, author or None)
            if book:
                print(f"Updated: {book}")
            else:
                print("Book not found.")
        elif choice == "4":
            book_id = int(input("Enter book ID to delete: "))
            book = manager.delete_book(book_id)
            if book:
                print(f"Deleted: {book}")
            else:
                print("Book not found.")
        elif choice == "5":
            title = input("Enter title to search: ")
            books = manager.list_books(by="title", value=title)
            for book in books:
                print(f"{book['id']}: {book['title']} by {book['author']}")
            if not books:
                print("No books found.")
        elif choice == "6":
            author = input("Enter author to search: ")
            books = manager.list_books(by="author", value=author)
            for book in books:
                print(f"{book['id']}: {book['title']} by {book['author']}")
            if not books:
                print("No books found.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
