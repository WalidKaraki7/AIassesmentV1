# 📚 Library Management System

A simple and intuitive web-based library management system built with Flask that allows users to manage books, track borrowing, and discover new titles through AI suggestions.

## 🚀 Features

### 📖 Book Management

- **Add Books**: Create new book entries with title, author, and genre
- **Edit Books**: Update existing book information
- **Delete Books**: Remove books from the library
- **View Books**: Browse all available books in a clean table format

### 🔍 Search & Discovery

- **Live Search**: Real-time search functionality as you type
- **Search Filters**: Search by title or author
- **AI Suggestions**: Get book recommendations across 5 genres:
  - Horror
  - Science Fiction
  - Fantasy
  - Romance
  - Mystery
- **Wikipedia Integration**: Direct links to Wikipedia pages for suggested books

### 🏃‍♂️ Borrowing System

- **Borrow Books**: Check out books from the available collection
- **Return Books**: Check books back into the library
- **Separate Views**:
  - **Main Library**: Shows only available books
  - **Borrowed Books**: Shows only currently borrowed books
- **Smart Workflow**: Borrowed books disappear from main list and appear in borrowed view

## 🛠️ Technologies Used

- **Backend**: Python 3.x with Flask framework
- **Database**: SQLite with automatic initialization
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **UI Framework**: Bootstrap 5.3.0
- **Template Engine**: Jinja2
- **HTTP Client**: Fetch API for AJAX requests

## 📁 Project Structure

```
AIassesmentV1/
├── app.py                 # Main Flask application
├── database.py           # Database operations and management
├── library/
│   ├── book_manager.py   # Business logic layer
│   └── __init__.py
├── templates/
│   ├── index.html        # Main library page
│   ├── borrowed_books.html # Borrowed books view
│   ├── add_book.html     # Add new book form
│   └── edit_book.html    # Edit book form
├── library.db            # SQLite database file
└── requirements.txt      # Python dependencies
```

## 🏃 How to Run

1. **Clone or download** the project files

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:

   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 📋 Usage

1. **Browse Books**: View all available books on the main page
2. **Add New Books**: Click "Add Book" to create new entries
3. **Search Books**: Use the search bar to find books by title or author
4. **Borrow Books**: Click "📖 Borrow" to check out a book
5. **View Borrowed**: Click "📚 Borrowed Books" to see checked-out items
6. **Return Books**: Use "↩️ Return Book" to check books back in
7. **AI Suggestions**: Click "🤖 AI Suggestions" for book recommendations

## 💾 Database

The system automatically creates and initializes a SQLite database with sample books on first run. The database stores:

- Book information (title, author, genre)
- Book status (available/borrowed)
- Unique book IDs for tracking

## 🎯 Key Features

- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Search**: Instant results as you type
- **Intuitive Workflow**: Clear separation between available and borrowed books
- **Sample Data**: Pre-populated with classic literature for testing
- **Error Handling**: Graceful error management and user feedback

---

_Built with ❤️ using Flask and modern web technologies_
