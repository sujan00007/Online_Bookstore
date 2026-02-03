"""Book CRUD operations"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import db, Book, Category
from app.routes.main import login_required

bp = Blueprint('books', __name__, url_prefix='/books')

def admin_required(f):
    """Decorator to restrict access to admin users"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login', 'warning')
            return redirect(url_for('auth.login'))
        if session.get('user_role') != 'admin':
            flash('Admin access required', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
def list_books():
    """List all books"""
    category_id = request.args.get('category', type=int)
    if category_id:
        books = Book.query.filter_by(category_id=category_id).all()
    else:
        books = Book.query.all()
    categories = Category.query.all()
    return render_template('books/list.html', books=books, categories=categories)

@bp.route('/<int:id>')
def detail(id):
    """Book detail page"""
    book = Book.query.get_or_404(id)
    return render_template('books/detail.html', book=book)

@bp.route('/manage')
@admin_required
def manage():
    """Manage books (admin only)"""
    books = Book.query.all()
    return render_template('books/manage.html', books=books)

@bp.route('/create', methods=['GET', 'POST'])
@admin_required
def create():
    """Create new book"""
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        price = request.form.get('price', type=float)
        stock = request.form.get('stock', type=int)
        description = request.form.get('description')
        category_id = request.form.get('category_id', type=int)
        
        if not all([title, author, price, stock, category_id]):
            flash('All fields are required', 'danger')
            return redirect(url_for('books.create'))
        
        book = Book(title=title, author=author, price=price, stock=stock,
                   description=description, category_id=category_id)
        db.session.add(book)
        db.session.commit()
        flash('Book created successfully', 'success')
        return redirect(url_for('books.manage'))
    
    categories = Category.query.all()
    return render_template('books/form.html', categories=categories, book=None)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit(id):
    """Edit existing book"""
    book = Book.query.get_or_404(id)
    
    if request.method == 'POST':
        book.title = request.form.get('title')
        book.author = request.form.get('author')
        book.price = request.form.get('price', type=float)
        book.stock = request.form.get('stock', type=int)
        book.description = request.form.get('description')
        book.category_id = request.form.get('category_id', type=int)
        
        db.session.commit()
        flash('Book updated successfully', 'success')
        return redirect(url_for('books.manage'))
    
    categories = Category.query.all()
    return render_template('books/form.html', categories=categories, book=book)

@bp.route('/delete/<int:id>', methods=['POST'])
@admin_required
def delete(id):
    """Delete book"""
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully', 'success')
    return redirect(url_for('books.manage'))
