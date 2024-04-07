from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *
from .models import *
from .forms import StockInForm




@login_required
def home(request):
    """Render the home page."""
    return render(request, 'home.html')

@login_required
def stock(request):
    """Display a list of all stock measurements."""
    stocks = StockMeasurement.objects.all()
    return render(request, 'stock.html', {'stocks': stocks})

@login_required
def manage_stock(request):
    """Add new stock measurement."""
    if request.method == 'POST':
        form = StockMeasurementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock added successfully.')
            return redirect('manage_stock')
        else:
            messages.error(request, 'Failed to add stock. Please check the form.')
    else:
        form = StockMeasurementForm()
    return render(request, 'manage_stock.html', {'form': form})

@login_required
def manage_product(request):
    """Add new product."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('manage_product')
        else:
            messages.error(request, 'Failed to add product. Please check the form.')
    else:
        form = ProductForm()
    return render(request, 'manage_product.html', {'form': form})

@login_required
def manage_profile(request):
    try:
        profile = request.user.profile  # Attempt to access the user's profile
    except Profile.DoesNotExist:
        profile = None  # If the profile does not exist, set it to None

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'manage_profile.html', {'form': form})

@login_required
def manage_price(request):
    """Add new price."""
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Price added successfully.')
            return redirect('manage_price')
        else:
            messages.error(request, 'Failed to add price. Please check the form.')
    else:
        form = PriceForm()
    return render(request, 'manage_price.html', {'form': form})

def manage_stocking(request):
    if request.method == 'POST':
        form = StockInForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock-in recorded successfully.')
            return redirect('manage_stocking')
        else:
            messages.error(request, 'Failed to record stock-in. Please check the form.')
    else:
        form = StockInForm()
    return render(request, 'manage_stocking.html', {'form': form})


@login_required
def manage_user(request):
    """Manage users."""
    users = User.objects.all()
    return render(request, 'manage_user.html', {'users': users})

@login_required
def per_group(request):
    """Display group-specific views."""
    # Logic for group-specific views
    return render(request, 'per_group.html')

@login_required
def prices(request):
    """Display prices."""
    prices = Prices.objects.all()
    return render(request, 'prices.html', {'prices': prices})

@login_required
def products(request):
    """Display products."""
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

@login_required
def profile(request):
    """Display user profile."""
    return render(request, 'profile.html')

@login_required
def reports(request):
    """Generate reports."""
    # Logic for generating reports
    return render(request, 'reports.html')

@login_required
def update_password(request):
    """Update user password."""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('update_password')
        else:
            messages.error(request, 'Failed to update password. Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'update_password.html', {'form': form})

@login_required
def update_status(request, product_id):
    """Update product status."""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductStatusForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product status updated successfully.')
            return redirect('manage_product')
        else:
            messages.error(request, 'Failed to update product status. Please check the form.')
    else:
        form = ProductStatusForm(instance=product)
    return render(request, 'update_status.html', {'form': form, 'product': product})

@login_required
def users(request):
    """Manage users."""
    # Logic for managing users (view, add, edit, delete)
    return render(request, 'users.html')

@login_required
def view_stock(request, stock_id):
    """View stock details."""
    stock = get_object_or_404(StockMeasurement, pk=stock_id)
    return render(request, 'view_stock.html', {'stock': stock})

@login_required
def view_price(request, price_id):
    """View price details."""
    price = get_object_or_404(Prices, pk=price_id)
    return render(request, 'view_price.html', {'price': price})

@login_required
def view_product(request, product_id):
    """View product details."""
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'view_product.html', {'product': product})

@login_required
def edit_user(request, user_id):
    """Edit user details."""
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User details updated successfully.')
            return redirect('manage_user')
        else:
            messages.error(request, 'Failed to update user details. Please check the form.')
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})

@login_required
def delete_user(request, user_id):
    """Delete user."""
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('manage_user')
    return render(request, 'delete_user.html', {'user': user})

@login_required
def edit_product(request, product_id):
    # Retrieve the product object from the database
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        # Populate the form with POST data and instance of the product
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            # Save the changes to the product
            form.save()
            return redirect('products')  # Redirect to the products list page
    else:
        # Populate the form with the existing product data
        form = ProductForm(instance=product)
    
    return render(request, 'edit_product.html', {'form': form, 'product': product})

@login_required
def delete_product(request, product_id):
    # Retrieve the product object from the database
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        # Delete the product
        product.delete()
        return redirect('products')  # Redirect to the products list page
    
    return render(request, 'delete_product.html', {'product': product})

@login_required
def edit_profile(request):
    try:
        profile = request.user.profile  # Attempt to access the user's profile
    except Profile.DoesNotExist:
        profile = None  # If the profile does not exist, set it to None

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})

@login_required
def sales_report(request):
    # Retrieve sales data from the database
    sales = Sale.objects.all()
    
    # Pass the sales data to the template
    return render(request, 'sales_report.html', {'sales': sales})

@login_required
def expense_report(request):
    # Retrieve expense data from the database
    expenses = Expense.objects.all()
    
    # Pass the expense data to the template
    return render(request, 'expense_report.html', {'expenses': expenses})

@login_required
def profit_loss_report(request):
    # Retrieve profit/loss data from the database
    profit_losses = ProfitLoss.objects.all()
    
    # Pass the profit/loss data to the template
    return render(request, 'profit_loss_report.html', {'profit_losses': profit_losses})

