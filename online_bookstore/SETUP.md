# Setup Instructions

## Quick Start Guide

### 1. Install Python
Ensure Python 3.7+ is installed:
```bash
python --version
```

### 2. Navigate to Project Directory
```bash
cd online_bookstore
```

### 3. Create Virtual Environment
```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Run the Application
```bash
python run.py
```

### 7. Open Browser
Navigate to: `http://localhost:5000`

## Demo Credentials

### Admin Access
- Email: `admin@bookstore.com`
- Password: `admin123`

### Customer Access
- Email: `john@example.com`
- Password: `customer123`

## Testing the Application

### As Customer:
1. Login with customer credentials
2. Browse books
3. Search for books
4. View book details
5. Place an order
6. View order history
7. Update profile
8. Cancel pending orders

### As Admin:
1. Login with admin credentials
2. Access "Manage Books"
3. Create new book
4. Edit existing book
5. Delete book
6. View all orders

## Project Features Checklist

- [x] User Registration & Login
- [x] Password Hashing
- [x] Session Management
- [x] User Dashboard
- [x] Profile Management
- [x] Book Listing with Categories
- [x] Book Search
- [x] Book Detail Page
- [x] CRUD Operations (Admin)
- [x] Order Placement
- [x] Order History
- [x] Order Cancellation
- [x] Stock Management
- [x] Client-side Validation
- [x] Server-side Validation
- [x] Flash Messages
- [x] Responsive Design
- [x] Navigation Menu
- [x] Footer
- [x] Contact Form

## Database Structure

The application automatically creates the database with sample data on first run.

### Tables:
1. **users** - User accounts
2. **categories** - Book categories
3. **books** - Book inventory
4. **orders** - Order records

### Relationships:
- User → Orders (One-to-Many)
- Category → Books (One-to-Many)
- Book → Orders (One-to-Many)

## Troubleshooting

### Issue: Port 5000 already in use
**Solution:** Change port in `run.py`:
```python
app.run(debug=True, port=5001)
```

### Issue: Module not found
**Solution:** Ensure virtual environment is activated and run:
```bash
pip install -r requirements.txt
```

### Issue: Database error
**Solution:** Delete `bookstore.db` file and restart application.

## File Structure Overview

```
online_bookstore/
├── app/                    # Application package
│   ├── __init__.py        # App factory & initialization
│   ├── models.py          # Database models
│   ├── routes/            # Route blueprints
│   ├── templates/         # HTML templates
│   └── static/            # CSS, JS, images
├── config.py              # Configuration
├── run.py                 # Entry point
├── requirements.txt       # Dependencies
└── README.md             # Documentation
```

## Next Steps

1. Explore all features
2. Test CRUD operations
3. Try different user roles
4. Customize styling
5. Add more features
6. Deploy to production

## Support

For issues or questions, refer to:
- README.md for detailed documentation
- Flask documentation: https://flask.palletsprojects.com/
- Bootstrap documentation: https://getbootstrap.com/
