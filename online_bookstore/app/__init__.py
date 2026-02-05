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
        # Fiction (10 books)
        Book(title='The Great Gatsby', author='F. Scott Fitzgerald', price=12.99, stock=50, 
             description='A classic American novel', category_id=1),
        Book(title='1984', author='George Orwell', price=14.99, stock=30,
             description='Dystopian social science fiction', category_id=1),
        Book(title='To Kill a Mockingbird', author='Harper Lee', price=13.99, stock=45,
             description='A gripping tale of racial injustice', category_id=1),
        Book(title='Pride and Prejudice', author='Jane Austen', price=11.99, stock=40,
             description='A romantic novel of manners', category_id=1),
        Book(title='The Catcher in the Rye', author='J.D. Salinger', price=12.49, stock=35,
             description='A story of teenage rebellion', category_id=1),
        Book(title='Harry Potter and the Sorcerer Stone', author='J.K. Rowling', price=19.99, stock=60,
             description='A young wizard discovers his magical heritage', category_id=1),
        Book(title='The Hobbit', author='J.R.R. Tolkien', price=15.99, stock=50,
             description='A fantasy adventure in Middle Earth', category_id=1),
        Book(title='The Lord of the Rings', author='J.R.R. Tolkien', price=29.99, stock=40,
             description='Epic fantasy trilogy', category_id=1),
        Book(title='Animal Farm', author='George Orwell', price=10.99, stock=55,
             description='A satirical allegorical novella', category_id=1),
        Book(title='Brave New World', author='Aldous Huxley', price=13.49, stock=38,
             description='Dystopian novel about a futuristic society', category_id=1),
        # Science (6 books)
        Book(title='A Brief History of Time', author='Stephen Hawking', price=18.99, stock=25,
             description='Popular science book on cosmology', category_id=2),
        Book(title='The Selfish Gene', author='Richard Dawkins', price=16.99, stock=30,
             description='Gene-centered view of evolution', category_id=2),
        Book(title='Cosmos', author='Carl Sagan', price=17.99, stock=28,
             description='Journey through space and time', category_id=2),
        Book(title='The Origin of Species', author='Charles Darwin', price=14.99, stock=32,
             description='Foundation of evolutionary biology', category_id=2),
        Book(title='Astrophysics for People in a Hurry', author='Neil deGrasse Tyson', price=15.99, stock=45,
             description='Quick guide to the universe', category_id=2),
        Book(title='The Double Helix', author='James Watson', price=13.99, stock=25,
             description='Discovery of DNA structure', category_id=2),
        # Technology (6 books)
        Book(title='Clean Code', author='Robert C. Martin', price=45.99, stock=40,
             description='A handbook of agile software craftsmanship', category_id=3),
        Book(title='The Pragmatic Programmer', author='Andrew Hunt', price=42.99, stock=35,
             description='Your journey to mastery', category_id=3),
        Book(title='Design Patterns', author='Gang of Four', price=49.99, stock=25,
             description='Elements of reusable object-oriented software', category_id=3),
        Book(title='Introduction to Algorithms', author='Thomas Cormen', price=89.99, stock=20,
             description='Comprehensive guide to algorithms', category_id=3),
        Book(title='Code Complete', author='Steve McConnell', price=54.99, stock=30,
             description='A practical handbook of software construction', category_id=3),
        Book(title='The Mythical Man-Month', author='Frederick Brooks', price=38.99, stock=28,
             description='Essays on software engineering', category_id=3),
        # History (5 books)
        Book(title='Sapiens', author='Yuval Noah Harari', price=22.99, stock=35,
             description='A brief history of humankind', category_id=4),
        Book(title='Guns Germs and Steel', author='Jared Diamond', price=20.99, stock=30,
             description='The fates of human societies', category_id=4),
        Book(title='The History of Ancient World', author='Susan Wise Bauer', price=24.99, stock=20,
             description='From earliest accounts to the fall of Rome', category_id=4),
        Book(title='A People History of the United States', author='Howard Zinn', price=19.99, stock=35,
             description='American history from the perspective of common people', category_id=4),
        Book(title='The Silk Roads', author='Peter Frankopan', price=21.99, stock=28,
             description='A new history of the world', category_id=4),
        # Biography (3 books)
        Book(title='Steve Jobs', author='Walter Isaacson', price=28.99, stock=20,
             description='The exclusive biography', category_id=5),
        Book(title='Becoming', author='Michelle Obama', price=26.99, stock=40,
             description='Memoir of former First Lady', category_id=5),
        Book(title='Einstein His Life and Universe', author='Walter Isaacson', price=27.99, stock=25,
             description='Biography of Albert Einstein', category_id=5)
    ]
    
    db.session.add_all(books)
    db.session.commit()
