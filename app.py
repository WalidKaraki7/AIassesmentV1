from flask import Flask, render_template, request, redirect, url_for, jsonify
from library.book_manager import BookManager

app = Flask(__name__)
manager = BookManager()

@app.route('/')
def index():
    books = manager.list_books()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form.get('genre', 'Unknown')
        manager.add_book(title, author, genre)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    books = manager.list_books()
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return redirect(url_for('index'))
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form.get('genre', book.get('genre', 'Unknown'))
        manager.edit_book(book_id, title, author, genre)
        return redirect(url_for('index'))
    return render_template('edit_book.html', book=book)

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    manager.delete_book(book_id)
    return redirect(url_for('index'))

@app.route('/search')
def search():
    query = request.args.get('q', '')
    by = request.args.get('by', 'title')
    books = manager.list_books(by=by, value=query) if query else manager.list_books()
    return render_template('index.html', books=books, query=query, by=by)

@app.route('/check_in/<int:book_id>')
def check_in_book(book_id):
    # Check in = borrow book (remove from main list)
    manager.check_in_book(book_id)
    return redirect(url_for('index'))

@app.route('/check_out/<int:book_id>')
def check_out_book(book_id):
    # Check out = return book (add back to main list)
    manager.check_out_book(book_id)
    return redirect(url_for('borrowed_books'))

@app.route('/borrowed')
def borrowed_books():
    books = manager.list_borrowed_books()
    return render_template('borrowed_books.html', books=books)

@app.route('/search_borrowed')
def search_borrowed():
    query = request.args.get('q', '')
    by = request.args.get('by', 'title')
    books = manager.list_borrowed_books(by=by, value=query) if query else manager.list_borrowed_books()
    return render_template('borrowed_books.html', books=books, query=query, by=by)

@app.route('/api/genre-suggestions')
def get_genre_suggestions():
    return jsonify(manager.get_genre_suggestions())

@app.route('/api/book-suggestions/<genre>')
def get_book_suggestions(genre):
    return jsonify(manager.get_book_suggestions(genre))

if __name__ == '__main__':
    app.run(debug=True)
