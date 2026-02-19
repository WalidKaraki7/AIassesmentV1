from flask import Flask, render_template, request, redirect, url_for, jsonify
from library.book_manager import BookManager

app = Flask(__name__)
manager = BookManager()

# Landing page route
@app.route('/')
def index():
    return render_template('index.html')

# Admin routes
@app.route('/admin')
def admin_index():
    available_books = manager.list_books()
    borrowed_books = manager.list_borrowed_books()
    # Combine and mark status
    all_books = []
    for book in available_books:
        book['status'] = 'available'
        all_books.append(book)
    for book in borrowed_books:
        book['status'] = 'borrowed'
        all_books.append(book)
    return render_template('admin.html', books=all_books)

@app.route('/admin/add', methods=['GET', 'POST'])
def admin_add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form.get('genre', 'Unknown')
        manager.add_book(title, author, genre)
        return redirect(url_for('admin_index'))
    return render_template('add_book.html')

@app.route('/admin/edit/<int:book_id>', methods=['GET', 'POST'])
def admin_edit_book(book_id):
    books = manager.list_books()
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return redirect(url_for('admin_index'))
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form.get('genre', book.get('genre', 'Unknown'))
        manager.edit_book(book_id, title, author, genre)
        return redirect(url_for('admin_index'))
    return render_template('edit_book.html', book=book)

@app.route('/admin/delete/<int:book_id>')
def admin_delete_book(book_id):
    manager.delete_book(book_id)
    return redirect(url_for('admin_index'))

@app.route('/admin/search')
def admin_search():
    query = request.args.get('q', '')
    by = request.args.get('by', 'title')
    available_books = manager.list_books(by=by, value=query) if query else manager.list_books()
    borrowed_books = manager.list_borrowed_books(by=by, value=query) if query else manager.list_borrowed_books()
    # Combine and mark status
    all_books = []
    for book in available_books:
        book['status'] = 'available'
        all_books.append(book)
    for book in borrowed_books:
        book['status'] = 'borrowed'
        all_books.append(book)
    return render_template('admin.html', books=all_books, query=query, by=by)

# Legacy routes (redirect to respective sections)
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    return redirect(url_for('admin_add_book'))

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    return redirect(url_for('admin_edit_book', book_id=book_id))

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    return redirect(url_for('admin_delete_book', book_id=book_id))

@app.route('/search')
def search():
    return redirect(url_for('admin_search'))

@app.route('/check_in/<int:book_id>')
def check_in_book(book_id):
    return redirect(url_for('customer_borrow_book', book_id=book_id))

# Customer routes
@app.route('/customer')
def customer_portal():
    available_books = manager.list_books()
    borrowed_books = manager.list_borrowed_books()
    # Combine and mark status
    all_books = []
    for book in available_books:
        book['status'] = 'available'
        all_books.append(book)
    for book in borrowed_books:
        book['status'] = 'borrowed'
        all_books.append(book)
    return render_template('customer.html', books=all_books)

@app.route('/customer/search')
def customer_search():
    query = request.args.get('q', '')
    by = request.args.get('by', 'title')
    available_books = manager.list_books(by=by, value=query) if query else manager.list_books()
    borrowed_books = manager.list_borrowed_books(by=by, value=query) if query else manager.list_borrowed_books()
    # Combine and mark status
    all_books = []
    for book in available_books:
        book['status'] = 'available'
        all_books.append(book)
    for book in borrowed_books:
        book['status'] = 'borrowed'
        all_books.append(book)
    return render_template('customer.html', books=all_books, query=query, by=by)

@app.route('/customer/borrow/<int:book_id>')
def customer_borrow_book(book_id):
    manager.check_in_book(book_id)
    return redirect(url_for('customer_portal'))

@app.route('/customer/return/<int:book_id>')
def customer_return_book(book_id):
    manager.check_out_book(book_id)
    return redirect(url_for('customer_portal'))

# API routes (unchanged)
@app.route('/api/genre-suggestions')
def get_genre_suggestions():
    return jsonify(manager.get_genre_suggestions())

@app.route('/api/book-suggestions/<genre>')
def get_book_suggestions(genre):
    return jsonify(manager.get_book_suggestions(genre))

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
