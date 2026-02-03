# Online Bookstore - Technical Documentation

## Project Overview

A full-stack web application for an online bookstore management system built using Flask framework with complete CRUD operations, user authentication, and responsive design.

## Architecture

### MVC Pattern
- **Models**: Database models in `app/models.py`
- **Views**: Jinja2 templates in `app/templates/`
- **Controllers**: Route handlers in `app/routes/`

### Blueprint Structure
The application uses Flask Blueprints for modular organization:
- `auth` - Authentication routes
- `main` - Main application routes
- `books` - Book management routes
- `orders` - Order management routes

## Database Design

### Entity Relationship Diagram

```
Users (1) ----< (M) Orders (M) >---- (1) Books
                                        |
                                        |
                                       (M)
                                        |
                                        |
                                    Categories (1)
```

### Table Schemas

#### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(200) NOT NULL,
    role VARCHAR(20) DEFAULT 'customer',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

#### Categories Table
```sql
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
```

#### Books Table
```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    stock INTEGER DEFAULT 0,
    description TEXT,
    category_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

#### Orders Table
```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    status VARCHAR(20) DEFAULT 'pending',
    total_price FLOAT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);
```

## API Routes

### Authentication Routes (`/auth`)

| Method | Route | Description | Auth Required |
|--------|-------|-------------|---------------|
| GET/POST | `/auth/register` | User registration | No |
| GET/POST | `/auth/login` | User login | No |
| GET | `/auth/logout` | User logout | Yes |

### Main Routes (`/`)

| Method | Route | Description | Auth Required |
|--------|-------|-------------|---------------|
| GET | `/` | Home page | No |
| GET | `/dashboard` | User dashboard | Yes |
| GET/POST | `/profile` | Profile management | Yes |
| GET/POST | `/contact` | Contact form | No |
| GET | `/search` | Search books | No |

### Book Routes (`/books`)

| Method | Route | Description | Auth Required |
|--------|-------|-------------|---------------|
| GET | `/books/` | List all books | No |
| GET | `/books/<id>` | Book details | No |
| GET | `/books/manage` | Manage books | Admin |
| GET/POST | `/books/create` | Create book | Admin |
| GET/POST | `/books/edit/<id>` | Edit book | Admin |
| POST | `/books/delete/<id>` | Delete book | Admin |

### Order Routes (`/orders`)

| Method | Route | Description | Auth Required |
|--------|-------|-------------|---------------|
| GET | `/orders/` | List user orders | Yes |
| POST | `/orders/create/<book_id>` | Create order | Yes |
| POST | `/orders/cancel/<id>` | Cancel order | Yes |

## Security Implementation

### 1. Password Security
- Passwords hashed using Werkzeug's `generate_password_hash()`
- SHA-256 algorithm with salt
- Never stored in plain text

```python
def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)
```

### 2. Session Management
- Server-side sessions using Flask's session object
- Session data stored securely
- Automatic session cleanup on logout

### 3. Route Protection
- Custom decorators for authentication
- Role-based access control
- Redirect to login for unauthorized access

```python
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function
```

### 4. Input Validation
- Client-side validation with JavaScript
- Server-side validation in Flask routes
- SQL injection prevention via SQLAlchemy ORM

## Form Validation

### Client-Side (JavaScript)
- Real-time validation
- Email format checking
- Password strength validation
- Password match confirmation
- Quantity range validation

### Server-Side (Flask)
- Required field validation
- Data type validation
- Unique constraint checking
- Business logic validation

## Frontend Technologies

### Bootstrap 5 Components Used
- Navbar (responsive navigation)
- Cards (book display)
- Forms (input handling)
- Tables (data display)
- Alerts (flash messages)
- Buttons (actions)
- Grid System (layout)
- Modal (confirmations)

### Custom CSS Features
- Hover effects on cards
- Smooth transitions
- Custom color scheme
- Responsive adjustments
- Custom scrollbar

### JavaScript Features
- Form validation
- Real-time feedback
- Confirmation dialogs
- Dynamic form handling

## Backend Technologies

### Flask Extensions
- **Flask-SQLAlchemy**: ORM for database operations
- **Werkzeug**: Password hashing and security

### Python Features Used
- Decorators (route protection)
- Context managers (database sessions)
- List comprehensions
- F-strings (formatting)
- Type hints (documentation)

## CRUD Operations Implementation

### Create (C)
```python
@bp.route('/create', methods=['GET', 'POST'])
@admin_required
def create():
    if request.method == 'POST':
        book = Book(...)
        db.session.add(book)
        db.session.commit()
```

### Read (R)
```python
@bp.route('/')
def list_books():
    books = Book.query.all()
    return render_template('books/list.html', books=books)
```

### Update (U)
```python
@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.title = request.form.get('title')
        db.session.commit()
```

### Delete (D)
```python
@bp.route('/delete/<int:id>', methods=['POST'])
@admin_required
def delete(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
```

## Template Inheritance

### Base Template Structure
```
base.html (navigation, footer, flash messages)
    ├── index.html (home page)
    ├── dashboard.html (user dashboard)
    ├── profile.html (user profile)
    ├── contact.html (contact form)
    ├── auth/
    │   ├── login.html
    │   └── register.html
    ├── books/
    │   ├── list.html
    │   ├── detail.html
    │   ├── manage.html
    │   └── form.html
    └── orders.html
```

## Responsive Design

### Breakpoints
- Mobile: < 768px
- Tablet: 768px - 991px
- Desktop: ≥ 992px

### Mobile Optimizations
- Collapsible navigation
- Stacked cards
- Touch-friendly buttons
- Optimized forms

## Error Handling

### Flash Messages
- Success (green)
- Warning (yellow)
- Danger (red)
- Info (blue)

### Error Pages
- 404 handling with `get_or_404()`
- Form validation errors
- Database constraint errors
- Authentication errors

## Performance Optimizations

1. **Database Queries**
   - Lazy loading for relationships
   - Query optimization
   - Index on foreign keys

2. **Frontend**
   - CDN for Bootstrap and icons
   - Minified CSS/JS
   - Efficient selectors

3. **Caching**
   - Static file caching
   - Browser caching headers

## Testing Scenarios

### User Registration
1. Valid registration
2. Duplicate email
3. Invalid email format
4. Password mismatch
5. Missing fields

### User Login
1. Valid credentials
2. Invalid credentials
3. Non-existent user

### Book Management (Admin)
1. Create book with valid data
2. Edit book information
3. Delete book
4. Validation errors

### Order Placement
1. Valid order
2. Insufficient stock
3. Invalid quantity
4. Order cancellation

## Deployment Checklist

- [ ] Set `debug=False`
- [ ] Use environment variables for secrets
- [ ] Configure production database
- [ ] Set up WSGI server
- [ ] Configure reverse proxy
- [ ] Enable HTTPS
- [ ] Set up logging
- [ ] Configure backups
- [ ] Set up monitoring
- [ ] Optimize static files

## Future Enhancements

1. **Features**
   - Shopping cart
   - Payment integration
   - Book reviews and ratings
   - Wishlist
   - Email notifications
   - Advanced search filters
   - Pagination

2. **Technical**
   - RESTful API
   - Database migrations (Flask-Migrate)
   - Unit tests
   - Integration tests
   - CI/CD pipeline
   - Docker containerization

3. **UI/UX**
   - Book cover images
   - Advanced filtering
   - Sorting options
   - User avatars
   - Dark mode

## Code Quality Standards

### Python (PEP 8)
- 4 spaces indentation
- Max line length: 79 characters
- Docstrings for functions
- Type hints where applicable

### HTML
- Semantic markup
- Proper indentation
- Accessibility attributes

### CSS
- BEM naming convention
- Organized by component
- Comments for sections

### JavaScript
- ES6+ syntax
- Descriptive variable names
- Function documentation

## Conclusion

This project demonstrates a complete full-stack web application with:
- Proper architecture and organization
- Security best practices
- Responsive design
- Complete CRUD operations
- User authentication and authorization
- Database relationships
- Form validation
- Error handling
- Clean, maintainable code

Perfect for university assessment and portfolio showcase.
