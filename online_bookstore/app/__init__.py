"""Flask application factory"""
from flask import Flask
from config import Config
from app.models import db

def create_app(config_class=Config):
    """Create and configure Flask application"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    from app.routes import auth, main, books, orders
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(books.bp)
    app.register_blueprint(orders.bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
        init_sample_data()
    
    return app

def init_sample_data():
    """Initialize database with sample data"""
    from app.models import User, Category, Book
    
    # Check if data already exists
    if User.query.first():
        return
    
    # Create admin user
    admin = User(name='Admin User', email='admin@bookstore.com', role='admin')
    admin.set_password('admin123')
    
    # Create customer user
    customer = User(name='John Doe', email='john@example.com', role='customer')
    customer.set_password('customer123')
    
    # Create categories
    categories = [
        Category(name='Fiction'),
        Category(name='Science'),
        Category(name='Technology'),
        Category(name='History'),
        Category(name='Biography')
    ]
    
    db.session.add(admin)
    db.session.add(customer)
    db.session.add_all(categories)
    db.session.commit()
    
    # Create sample books
    books = [
        Book(title='The Great Gatsby', author='F. Scott Fitzgerald', price=12.99, stock=50, 
             description='A classic American novel', category_id=1),
        Book(title='1984', author='George Orwell', price=14.99, stock=30,
             description='Dystopian social science fiction', category_id=1),
        Book(title='A Brief History of Time', author='Stephen Hawking', price=18.99, stock=25,
             description='Popular science book on cosmology', category_id=2),
        Book(title='Clean Code', author='Robert C. Martin', price=45.99, stock=40,
             description='A handbook of agile software craftsmanship', category_id=3),
        Book(title='Sapiens', author='Yuval Noah Harari', price=22.99, stock=35,
             description='A brief history of humankind', category_id=4),
        Book(title='Steve Jobs', author='Walter Isaacson', price=28.99, stock=20,
             description='The exclusive biography', category_id=5)
    ]
    
    db.session.add_all(books)
    db.session.commit()
