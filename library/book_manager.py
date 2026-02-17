import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

class BookManager:
    def __init__(self):
        self.db = DatabaseManager()
        
        # AI suggestion data
        self.genre_suggestions = [
            "Horror", "Science Fiction", "Fantasy", "Romance", "Mystery"
        ]
        
        self.book_suggestions = {
            "Horror": [
                {"title": "The Shining", "author": "Stephen King", "wikipedia": "https://en.wikipedia.org/wiki/The_Shining_(novel)"},
                {"title": "Dracula", "author": "Bram Stoker", "wikipedia": "https://en.wikipedia.org/wiki/Dracula"},
                {"title": "Frankenstein", "author": "Mary Shelley", "wikipedia": "https://en.wikipedia.org/wiki/Frankenstein"},
                {"title": "The Exorcist", "author": "William Peter Blatty", "wikipedia": "https://en.wikipedia.org/wiki/The_Exorcist_(novel)"},
                {"title": "Pet Sematary", "author": "Stephen King", "wikipedia": "https://en.wikipedia.org/wiki/Pet_Sematary"}
            ],
            "Science Fiction": [
                {"title": "Dune", "author": "Frank Herbert", "wikipedia": "https://en.wikipedia.org/wiki/Dune_(novel)"},
                {"title": "Foundation", "author": "Isaac Asimov", "wikipedia": "https://en.wikipedia.org/wiki/Foundation_(Asimov_novel)"},
                {"title": "Ender's Game", "author": "Orson Scott Card", "wikipedia": "https://en.wikipedia.org/wiki/Ender%27s_Game"},
                {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "wikipedia": "https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy"},
                {"title": "Neuromancer", "author": "William Gibson", "wikipedia": "https://en.wikipedia.org/wiki/Neuromancer"}
            ],
            "Fantasy": [
                {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "wikipedia": "https://en.wikipedia.org/wiki/The_Lord_of_the_Rings"},
                {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "wikipedia": "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone"},
                {"title": "A Game of Thrones", "author": "George R.R. Martin", "wikipedia": "https://en.wikipedia.org/wiki/A_Game_of_Thrones"},
                {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "wikipedia": "https://en.wikipedia.org/wiki/The_Name_of_the_Wind"},
                {"title": "The Way of Kings", "author": "Brandon Sanderson", "wikipedia": "https://en.wikipedia.org/wiki/The_Way_of_Kings"}
            ],
            "Romance": [
                {"title": "Pride and Prejudice", "author": "Jane Austen", "wikipedia": "https://en.wikipedia.org/wiki/Pride_and_Prejudice"},
                {"title": "The Notebook", "author": "Nicholas Sparks", "wikipedia": "https://en.wikipedia.org/wiki/The_Notebook"},
                {"title": "Outlander", "author": "Diana Gabaldon", "wikipedia": "https://en.wikipedia.org/wiki/Outlander_(novel)"},
                {"title": "Me Before You", "author": "Jojo Moyes", "wikipedia": "https://en.wikipedia.org/wiki/Me_Before_You"},
                {"title": "The Kiss Quotient", "author": "Helen Hoang", "wikipedia": "https://en.wikipedia.org/wiki/The_Kiss_Quotient"}
            ],
            "Mystery": [
                {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "wikipedia": "https://en.wikipedia.org/wiki/The_Girl_with_the_Dragon_Tattoo"},
                {"title": "Gone Girl", "author": "Gillian Flynn", "wikipedia": "https://en.wikipedia.org/wiki/Gone_Girl_(novel)"},
                {"title": "The Da Vinci Code", "author": "Dan Brown", "wikipedia": "https://en.wikipedia.org/wiki/The_Da_Vinci_Code"},
                {"title": "And Then There Were None", "author": "Agatha Christie", "wikipedia": "https://en.wikipedia.org/wiki/And_Then_There_Were_None"},
                {"title": "The Big Sleep", "author": "Raymond Chandler", "wikipedia": "https://en.wikipedia.org/wiki/The_Big_Sleep"}
            ]
        }

    def list_books(self, by=None, value=None):
        books = self.db.get_available_books()  # Only show available books on main page
        if by and value:
            return [book for book in books if value.lower() in str(book.get(by, "")).lower()]
        return books
    
    def list_borrowed_books(self, by=None, value=None):
        books = self.db.get_borrowed_books()
        if by and value:
            return [book for book in books if value.lower() in str(book.get(by, "")).lower()]
        return books

    def add_book(self, title, author, genre="Unknown"):
        book_id = self.db.add_book(title, author, genre)
        return {"id": book_id, "title": title, "author": author, "genre": genre, "status": "available"}

    def edit_book(self, book_id, title=None, author=None, genre=None):
        self.db.update_book(book_id, title, author, genre)
        # Return updated book (simplified)
        books = self.db.get_all_books()
        return next((book for book in books if book["id"] == book_id), None)

    def delete_book(self, book_id):
        self.db.delete_book(book_id)
        return True

    def check_out_book(self, book_id):
        # Check out = return book (borrowed -> available)
        self.db.update_book_status(book_id, "available")
        return True

    def check_in_book(self, book_id):
        # Check in = borrow book (available -> borrowed)
        self.db.update_book_status(book_id, "borrowed")
        return True
    
    def get_genre_suggestions(self):
        return self.genre_suggestions
    
    def get_book_suggestions(self, genre):
        return self.book_suggestions.get(genre, [])
