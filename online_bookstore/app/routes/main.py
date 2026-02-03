"""Main application routes"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import db, User, Book
from functools import wraps

bp = Blueprint('main', __name__)

def login_required(f):
    """Decorator to protect routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
def index():
    """Home page with featured books"""
    books = Book.query.limit(6).all()
    return render_template('index.html', books=books)

@bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    user = User.query.get(session['user_id'])
    recent_orders = user.orders[-5:] if user.orders else []
    return render_template('dashboard.html', user=user, orders=recent_orders)

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """User profile management"""
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        user.name = request.form.get('name')
        email = request.form.get('email')
        
        # Check if email is taken by another user
        existing = User.query.filter_by(email=email).first()
        if existing and existing.id != user.id:
            flash('Email already in use', 'danger')
            return redirect(url_for('main.profile'))
        
        user.email = email
        
        # Update password if provided
        new_password = request.form.get('new_password')
        if new_password:
            user.set_password(new_password)
        
        db.session.commit()
        session['user_name'] = user.name
        flash('Profile updated successfully', 'success')
        return redirect(url_for('main.profile'))
    
    return render_template('profile.html', user=user)

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact form"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if name and email and message:
            flash('Thank you for contacting us! We will get back to you soon.', 'success')
            return redirect(url_for('main.contact'))
        else:
            flash('Please fill all fields', 'danger')
    
    return render_template('contact.html')

@bp.route('/search')
def search():
    """Search books"""
    query = request.args.get('q', '')
    if query:
        books = Book.query.filter(
            (Book.title.contains(query)) | (Book.author.contains(query))
        ).all()
    else:
        books = []
    return render_template('books/list.html', books=books, search_query=query)
