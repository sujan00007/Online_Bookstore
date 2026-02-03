/**
 * Client-side form validation
 */

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    
    // Get all forms that need validation
    const forms = document.querySelectorAll('form[novalidate]');
    
    // Loop through forms and add validation
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', function(event) {
            // Check form validity
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            // Add Bootstrap validation classes
            form.classList.add('was-validated');
            
            // Custom validation for specific forms
            if (form.id === 'registerForm') {
                validatePasswordMatch(event, form);
            }
            
            if (form.id === 'orderForm') {
                validateOrderQuantity(event, form);
            }
        }, false);
    });
    
    // Real-time email validation
    const emailInputs = document.querySelectorAll('input[type="email"]');
    emailInputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateEmail(this);
        });
    });
    
    // Real-time password validation
    const passwordInputs = document.querySelectorAll('input[type="password"]');
    passwordInputs.forEach(input => {
        input.addEventListener('input', function() {
            validatePassword(this);
        });
    });
});

/**
 * Validate password match in registration form
 */
function validatePasswordMatch(event, form) {
    const password = form.querySelector('#password');
    const confirmPassword = form.querySelector('#confirm_password');
    
    if (confirmPassword && password) {
        if (password.value !== confirmPassword.value) {
            confirmPassword.setCustomValidity('Passwords do not match');
            event.preventDefault();
            event.stopPropagation();
        } else {
            confirmPassword.setCustomValidity('');
        }
    }
}

/**
 * Validate email format
 */
function validateEmail(input) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (input.value && !emailRegex.test(input.value)) {
        input.setCustomValidity('Please enter a valid email address');
    } else {
        input.setCustomValidity('');
    }
}

/**
 * Validate password strength
 */
function validatePassword(input) {
    if (input.value.length > 0 && input.value.length < 6) {
        input.setCustomValidity('Password must be at least 6 characters');
    } else {
        input.setCustomValidity('');
    }
}

/**
 * Validate order quantity
 */
function validateOrderQuantity(event, form) {
    const quantityInput = form.querySelector('#quantity');
    if (quantityInput) {
        const quantity = parseInt(quantityInput.value);
        const max = parseInt(quantityInput.getAttribute('max'));
        const min = parseInt(quantityInput.getAttribute('min'));
        
        if (quantity < min || quantity > max) {
            quantityInput.setCustomValidity(`Quantity must be between ${min} and ${max}`);
            event.preventDefault();
            event.stopPropagation();
        } else {
            quantityInput.setCustomValidity('');
        }
    }
}

/**
 * Confirm delete actions
 */
function confirmDelete(message) {
    return confirm(message || 'Are you sure you want to delete this item?');
}
