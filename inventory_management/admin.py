from django.contrib import admin
from .models import Department, StockMeasurement, FruitVegetable, OtherItem, Product, StockIn, Sale, Expense, ProfitLoss,Prices,Profile


@admin.register(Prices)
class PricesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    list_filter = ['price']
    ordering = ['name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(StockMeasurement)
class StockMeasurementAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'added_by', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(FruitVegetable)
class FruitVegetableAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'unit', 'added_by', 'created_at', 'updated_at')
    search_fields = ('name', 'category',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(OtherItem)
class OtherItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'unit', 'added_by', 'created_at', 'updated_at')
    search_fields = ('name', 'category',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'department', 'status', 'delete_flag', 'date_added', 'date_updated')
    list_filter = ('department', 'status', 'delete_flag')
    search_fields = ('name', 'description',)
    date_hierarchy = 'date_added'
    fieldsets = (
        (None, {'fields': ('name', 'description', 'price', 'department')}),
        ('Status and Flags', {'fields': ('status', 'delete_flag')}),
    )

@admin.register(StockIn)
class StockInAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('product__name',)
    date_hierarchy = 'date_added'

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'amount', 'date_sold')
    list_filter = ('date_sold',)
    search_fields = ('product__name',)
    date_hierarchy = 'date_sold'

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date_added')
    search_fields = ('description',)
    date_hierarchy = 'date_added'

@admin.register(ProfitLoss)
class ProfitLossAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date_added')
    search_fields = ('description',)
    date_hierarchy = 'date_added'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'location', 'birth_date']
    search_fields = ['user__username', 'bio', 'location']
    list_filter = ['birth_date']


