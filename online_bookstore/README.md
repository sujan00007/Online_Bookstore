# Online Bookstore Website

A complete full-stack web application for an online bookstore built with Flask, Bootstrap, and SQLite.

## 🎓 University Project

This project demonstrates a complete web development solution using modern technologies and best practices.

## 🚀 Features

- **User Authentication**: Registration, login, logout with password hashing
- **User Roles**: Customer and Admin roles with different permissions
- **Book Management**: Full CRUD operations for books (Admin only)
- **Order System**: Place orders, view order history, cancel pending orders
- **Search Functionality**: Search books by title or author
- **Category Filtering**: Browse books by categories
- **Responsive Design**: Mobile-first design using Bootstrap 5
- **Form Validation**: Client-side and server-side validation
- **Flash Messages**: User feedback for all actions
- **Protected Routes**: Authentication required for certain pages
- **Profile Management**: Update user profile and password

## 🛠️ Tech Stack

### Frontend
- HTML5 (Semantic markup)
- CSS3 (Custom styling)
- Bootstrap 5 (Responsive framework)
- JavaScript (Form validation & interactivity)

### Backend
- Python 3.x
- Flask (Web framework)
- Flask-SQLAlchemy (ORM)
- Jinja2 (Template engine)
- Werkzeug (Password hashing)

### Database
- SQLite (Development database)

## 📁 Project Structure

```
online_bookstore/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication routes
│   │   ├── main.py          # Main routes
│   │   ├── books.py         # Book CRUD
│   │   └── orders.py        # Order management
│   ├── templates/           # Jinja2 templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── auth/
│   │   ├── books/
│   │   └── ...
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── validation.js
├── config.py                # Configuration
├── run.py                   # Application entry point
├── requirements.txt         # Dependencies
└── README.md
```

## 📊 Database Schema

### Users Table
- id (Primary Key)
- name
- email (Unique)
- password_hash
- role (customer/admin)
- created_at

### Categories Table
- id (Primary Key)
- name (Unique)

### Books Table
- id (Primary Key)
- title
- author
- price
- stock
- description
- category_id (Foreign Key)
- created_at

### Orders Table
- id (Primary Key)
- user_id (Foreign Key)
- book_id (Foreign Key)
- quantity
- total_price
- status (pending/completed/cancelled)
- created_at

## 🔧 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone or Download
```bash
cd online_bookstore
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python run.py
```

### Step 5: Access the Application
Open your browser and navigate to:
```
http://localhost:5000
```

## 👤 Demo Accounts

### Admin Account
- Email: `admin@bookstore.com`
- Password: `admin123`
- Access: Full CRUD operations on books

### Customer Account
- Email: `john@example.com`
- Password: `customer123`
- Access: Browse and order books

## 📱 Pages & Routes

| Page | Route | Description | Auth Required |
|------|-------|-------------|---------------|
| Home | `/` | Landing page with featured books | No |
| Books List | `/books/` | All books with category filter | No |
| Book Detail | `/books/<id>` | Individual book details | No |
| Search | `/search?q=query` | Search results | No |
| Login | `/auth/login` | User login | No |
| Register | `/auth/register` | User registration | No |
| Dashboard | `/dashboard` | User dashboard | Yes |
| Profile | `/profile` | User profile management | Yes |
| My Orders | `/orders/` | User order history | Yes |
| Contact | `/contact` | Contact form | No |
| Manage Books | `/books/manage` | Book management (Admin) | Yes (Admin) |
| Add Book | `/books/create` | Create new book (Admin) | Yes (Admin) |
| Edit Book | `/books/edit/<id>` | Edit book (Admin) | Yes (Admin) |

## ✨ Key Features Explained

### 1. Authentication System
- Password hashing using Werkzeug
- Session-based authentication
- Protected routes with decorators
- Role-based access control

### 2. CRUD Operations
- **Create**: Add new books (Admin)
- **Read**: View all books and details
- **Update**: Edit book information (Admin)
- **Delete**: Remove books (Admin)

### 3. Order Management
- Place orders with quantity selection
- Stock validation
- Order history tracking
- Cancel pending orders
- Automatic stock updates

### 4. Form Validation
- Client-side validation with JavaScript
- Server-side validation in Flask
- Real-time feedback
- Custom validation messages

### 5. Responsive Design
- Mobile-first approach
- Bootstrap grid system
- Responsive navigation
- Optimized for all screen sizes

## 🔒 Security Features

- Password hashing (never store plain text)
- CSRF protection (Flask built-in)
- SQL injection prevention (SQLAlchemy ORM)
- Session management
- Input validation and sanitization
- Role-based access control

## 🎨 Customization

### Change Database
Edit `config.py`:
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///bookstore.db'
```

### Add More Categories
Access admin account and modify the database or update `app/__init__.py`

### Modify Styling
Edit `app/static/css/style.css`

## 📝 Development Notes

### Adding New Features
1. Create route in appropriate blueprint
2. Create corresponding template
3. Update navigation in `base.html`
4. Add validation if needed

### Database Migrations
For production, consider using Flask-Migrate:
```bash
pip install Flask-Migrate
```

## 🐛 Troubleshooting

### Database Issues
Delete `bookstore.db` and restart the application to recreate with sample data.

### Port Already in Use
Change port in `run.py`:
```python
app.run(debug=True, port=5001)
```

### Module Not Found
Ensure virtual environment is activated and dependencies are installed.

## 📚 Learning Outcomes

This project demonstrates:
- Flask application structure and blueprints
- Database design and relationships
- ORM usage with SQLAlchemy
- Template inheritance with Jinja2
- Form handling and validation
- Session management
- RESTful routing
- Responsive web design
- Security best practices

## 🚀 Deployment

### For Production:
1. Set `debug=False` in `run.py`
2. Use environment variables for SECRET_KEY
3. Use production database (PostgreSQL/MySQL)
4. Use WSGI server (Gunicorn/uWSGI)
5. Set up reverse proxy (Nginx)
6. Enable HTTPS

### Deployment Platforms:
- Heroku
- PythonAnywhere
- AWS Elastic Beanstalk
- DigitalOcean
- Render

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Author

University Project - Online Bookstore Website

## 🙏 Acknowledgments

- Flask Documentation
- Bootstrap Documentation
- SQLAlchemy Documentation
- Stack Overflow Community

---

**Note**: This is a university project for educational purposes. For production use, additional security measures and optimizations should be implemented.
