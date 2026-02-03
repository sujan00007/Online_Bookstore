"""Order management routes"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import db, Order, Book, User
from app.routes.main import login_required

bp = Blueprint('orders', __name__, url_prefix='/orders')

@bp.route('/')
@login_required
def list_orders():
    """List user orders"""
    user = User.query.get(session['user_id'])
    orders = user.orders
    return render_template('orders.html', orders=orders)

@bp.route('/create/<int:book_id>', methods=['POST'])
@login_required
def create(book_id):
    """Create new order"""
    book = Book.query.get_or_404(book_id)
    quantity = request.form.get('quantity', 1, type=int)
    
    # Validate stock
    if quantity > book.stock:
        flash('Insufficient stock available', 'danger')
        return redirect(url_for('books.detail', id=book_id))
    
    # Create order
    total_price = book.price * quantity
    order = Order(
        user_id=session['user_id'],
        book_id=book_id,
        quantity=quantity,
        total_price=total_price,
        status='pending'
    )
    
    # Update stock
    book.stock -= quantity
    
    db.session.add(order)
    db.session.commit()
    
    flash('Order placed successfully!', 'success')
    return redirect(url_for('orders.list_orders'))

@bp.route('/cancel/<int:id>', methods=['POST'])
@login_required
def cancel(id):
    """Cancel order"""
    order = Order.query.get_or_404(id)
    
    # Verify ownership
    if order.user_id != session['user_id']:
        flash('Unauthorized action', 'danger')
        return redirect(url_for('orders.list_orders'))
    
    if order.status == 'pending':
        # Restore stock
        book = Book.query.get(order.book_id)
        book.stock += order.quantity
        
        order.status = 'cancelled'
        db.session.commit()
        flash('Order cancelled successfully', 'success')
    else:
        flash('Cannot cancel this order', 'warning')
    
    return redirect(url_for('orders.list_orders'))
