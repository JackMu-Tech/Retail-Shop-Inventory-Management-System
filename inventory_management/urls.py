from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stock/', views.stock, name='stock'),
    path('manage_stock/', views.manage_stock, name='manage_stock'),
    path('manage_product/', views.manage_product, name='manage_product'),
    path('manage_profile/', views.manage_profile, name='manage_profile'),
    path('manage_price/', views.manage_price, name='manage_price'),
    path('manage_stocking/', views.manage_stocking, name='manage_stocking'),
    path('manage_user/', views.manage_user, name='manage_user'),
    path('per_group/', views.per_group, name='per_group'),
    path('prices/', views.prices, name='prices'),
    path('products/', views.products, name='products'),
    path('profile/', views.profile, name='profile'),
    path('reports/', views.reports, name='reports'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_status/<int:product_id>/', views.update_status, name='update_status'),
    path('users/', views.users, name='users'),
    path('view_stock/<int:stock_id>/', views.view_stock, name='view_stock'),
    path('view_price/<int:price_id>/', views.view_price, name='view_price'),
    path('view_product/<int:product_id>/', views.view_product, name='view_product'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),  # Edit user path
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),  # Delete user path
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),  # Edit product path
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),  # Delete product path
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # Edit profile path
    path('sales_report/', views.sales_report, name='sales_report'),  # Sales report path
    path('expense_report/', views.expense_report, name='expense_report'),  # Expense report path
    path('profit_loss_report/', views.profit_loss_report, name='profit_loss_report'),  # Profit/loss report path
]
