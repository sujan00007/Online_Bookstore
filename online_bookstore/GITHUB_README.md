# 📚 Online Bookstore Website

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Complete-success.svg)

A complete full-stack web application for an online bookstore built with Flask, Bootstrap, and SQLite. Perfect for university projects and portfolio showcase.

## 🌟 Features

- ✅ **User Authentication** - Secure registration, login, and logout
- ✅ **Role-Based Access** - Customer and Admin roles with different permissions
- ✅ **Book Management** - Full CRUD operations (Admin only)
- ✅ **Order System** - Place orders, view history, cancel pending orders
- ✅ **Search & Filter** - Search books by title/author, filter by category
- ✅ **Professional Design** - Clean, modern UI with navy blue color scheme
- ✅ **Responsive Design** - Mobile-first design using Bootstrap 5
- ✅ **Form Validation** - Client-side (JavaScript) and server-side (Flask)
- ✅ **Flash Messages** - User feedback for all actions
- ✅ **Profile Management** - Update user information and password
- ✅ **Stock Management** - Automatic inventory tracking

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/online-bookstore.git
cd online-bookstore

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py

# Open browser
http://localhost:5000
```

## 👤 Demo Accounts

| Role | Email | Password | Access |
|------|-------|----------|--------|
| Admin | admin@bookstore.com | admin123 | Full CRUD + All features |
| Customer | john@example.com | customer123 | Browse & Order books |

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
- SQLite (4 related tables)

## 📊 Database Schema

```
Users (1) ────< Orders (M) >──── Books (M)
                                    │
                                    │
                                Categories (1)
```

### Tables
- **Users**: id, name, email, password_hash, role, created_at
- **Categories**: id, name
- **Books**: id, title, author, price, stock, description, category_id, created_at
- **Orders**: id, user_id, book_id, quantity, status, total_price, created_at

## 📁 Project Structure

```
online_bookstore/
├── app/
│   ├── routes/              # Blueprints (auth, main, books, orders)
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── books.py
│   │   ├── main.py
│   │   └── orders.py
│   ├── templates/           # Jinja2 HTML templates
│   │   ├── auth/
│   │   ├── books/
│   │   └── ...
│   ├── static/              # CSS, JavaScript
│   │   ├── css/
│   │   └── js/
│   ├── __init__.py         # App factory
│   └── models.py           # Database models
├── config.py               # Configuration
├── run.py                  # Entry point
├── requirements.txt        # Dependencies
└── README.md              # Documentation
```

## 📄 Pages

1. **Home** (/) - Landing page with featured books
2. **Books List** (/books/) - All books with category filtering
3. **Book Detail** (/books/<id>) - Individual book information
4. **Search** (/search) - Search results
5. **Login** (/auth/login) - User authentication
6. **Register** (/auth/register) - New user signup
7. **Dashboard** (/dashboard) - User dashboard
8. **Profile** (/profile) - Profile management
9. **My Orders** (/orders/) - Order history
10. **Contact** (/contact) - Contact form
11. **Manage Books** (/books/manage) - Admin panel
12. **Add/Edit Book** (/books/create, /books/edit/<id>) - Book forms

## 🔒 Security Features

- Password hashing using SHA-256
- Session-based authentication
- Protected routes with decorators
- Role-based access control
- SQL injection prevention (ORM)
- XSS protection (Jinja2 auto-escaping)
- CSRF protection (Flask built-in)
- Input validation (client + server)

## 📱 Responsive Design

- **Mobile** (< 768px): Single column, hamburger menu
- **Tablet** (768px - 991px): Two columns, optimized layout
- **Desktop** (≥ 992px): Three columns, full navigation

## 🧪 Testing

### As Customer
1. Register/Login
2. Browse books
3. Search books
4. View book details
5. Place orders
6. View order history
7. Cancel pending orders
8. Update profile

### As Admin
1. Login as admin
2. Access "Manage Books"
3. Create new book
4. Edit existing book
5. Delete book
6. View all features

## 📚 Documentation

- **README.md** - Main documentation
- **SETUP.md** - Detailed setup instructions
- **PROJECT_DOCUMENTATION.md** - Technical documentation
- **FEATURES_CHECKLIST.md** - Feature verification
- **QUICK_START.txt** - Quick reference
- **PRESENTATION_GUIDE.md** - Presentation script

## 🎯 Requirements Met

| Requirement | Required | Implemented | Status |
|-------------|----------|-------------|--------|
| Pages | 5 | 12 | ✅ 240% |
| Tables | 3 | 4 | ✅ 133% |
| CRUD | Yes | Complete | ✅ 100% |
| Authentication | Yes | Complete | ✅ 100% |
| Validation | Both | Both | ✅ 100% |
| Responsive | Yes | Full | ✅ 100% |

## 🚀 Deployment

### Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
git push heroku main
```

### PythonAnywhere
1. Upload files
2. Create virtual environment
3. Configure WSGI
4. Set environment variables

### Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "run.py"]
```

## 🔧 Configuration

Edit `config.py` for custom settings:

```python
class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bookstore.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Sujan Bharati**
- Location: Kathmandu, Nepal
- Email: sujanbharati00@gmail.com
- Phone: +977 9847258796

## 🙏 Acknowledgments

- Flask Documentation
- Bootstrap Documentation
- SQLAlchemy Documentation
- Stack Overflow Community

## 📞 Support

For support, email sujanbharati00@gmail.com or open an issue on GitHub.

## 🌟 Show your support

Give a ⭐️ if this project helped you!

---

**Made with ❤️ in Kathmandu, Nepal**
