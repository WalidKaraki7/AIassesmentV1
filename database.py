import sqlite3
import os

def init_db():
    """Initialize the database with books table"""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT,
            status TEXT DEFAULT 'available'
        )
    ''')
    
    # Check if table is empty and add sample data
    cursor.execute('SELECT COUNT(*) FROM books')
    count = cursor.fetchone()[0]
    
    if count == 0:
        sample_books = [
            ("1984", "George Orwell", "Dystopian Fiction", "available"),
            ("To Kill a Mockingbird", "Harper Lee", "Classic Literature", "available"),
            ("The Great Gatsby", "F. Scott Fitzgerald", "Classic Literature", "borrowed")
        ]
        
        cursor.executemany(
            'INSERT INTO books (title, author, genre, status) VALUES (?, ?, ?, ?)',
            sample_books
        )
    
    conn.commit()
    conn.close()

class DatabaseManager:
    def __init__(self):
        init_db()
    
    def get_connection(self):
        return sqlite3.connect('library.db')
    
    def get_all_books(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = []
        for row in cursor.fetchall():
            books.append({
                'id': row[0],
                'title': row[1],
                'author': row[2],
                'genre': row[3],
                'status': row[4]
            })
        conn.close()
        return books
    
    def add_book(self, title, author, genre="Unknown"):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO books (title, author, genre, status) VALUES (?, ?, ?, ?)',
            (title, author, genre, 'available')
        )
        book_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return book_id
    
    def update_book(self, book_id, title=None, author=None, genre=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if title:
            updates.append('title = ?')
            params.append(title)
        if author:
            updates.append('author = ?')
            params.append(author)
        if genre:
            updates.append('genre = ?')
            params.append(genre)
        
        if updates:
            params.append(book_id)
            cursor.execute(
                f'UPDATE books SET {", ".join(updates)} WHERE id = ?',
                params
            )
        
        conn.commit()
        conn.close()
    
    def delete_book(self, book_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()
        conn.close()
    
    def update_book_status(self, book_id, status):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE books SET status = ? WHERE id = ?',
            (status, book_id)
        )
        conn.commit()
        conn.close()
    
    def get_available_books(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books WHERE status = "available"')
        books = []
        for row in cursor.fetchall():
            books.append({
                'id': row[0],
                'title': row[1],
                'author': row[2],
                'genre': row[3],
                'status': row[4]
            })
        conn.close()
        return books
    
    def get_borrowed_books(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books WHERE status = "borrowed"')
        books = []
        for row in cursor.fetchall():
            books.append({
                'id': row[0],
                'title': row[1],
                'author': row[2],
                'genre': row[3],
                'status': row[4]
            })
        conn.close()
        return books