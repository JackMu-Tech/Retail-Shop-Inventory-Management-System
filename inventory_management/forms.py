from django import forms
from django.contrib.auth.models import User
from django.forms import formset_factory
from .models import Product, StockMeasurement, FruitVegetable, OtherItem, Expense, ProfitLoss,Prices, StockIn,Profile


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'department', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class StockMeasurementForm(forms.ModelForm):
    class Meta:
        model = StockMeasurement
        fields = ['name', 'quantity', 'unit']
        labels = {
            'name': 'Stock Name',
            'quantity': 'Stock Quantity',
            'unit': 'Unit of Measurement',
        }
        help_texts = {
            'quantity': 'Enter the stock quantity in kg or litres.',
        }
        error_messages = {
            'quantity': {
                'max_value': 'Please enter a valid quantity.',
            }
        }

class FruitVegetableForm(forms.ModelForm):
    class Meta:
        model = FruitVegetable
        fields = ['name', 'category', 'quantity', 'unit']

class OtherItemForm(forms.ModelForm):
    class Meta:
        model = OtherItem
        fields = ['name', 'category', 'quantity', 'unit']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount']

class ProfitLossForm(forms.ModelForm):
    class Meta:
        model = ProfitLoss
        fields = ['description', 'amount']

class StockInForm(forms.ModelForm):
    class Meta:
        model = StockIn
        fields = ['product', 'quantity', 'date_added']  


class PriceForm(forms.ModelForm):
    class Meta:
        model = Prices
        fields = ['name', 'price']
        labels = {
            'name': 'Name',
            'price': 'Price',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']



# Formsets for handling multiple records in a single form
StockMeasurementFormSet = formset_factory(StockMeasurementForm, extra=3)
FruitVegetableFormSet = formset_factory(FruitVegetableForm, extra=3)
OtherItemFormSet = formset_factory(OtherItemForm, extra=3)
ExpenseFormSet = formset_factory(ExpenseForm, extra=3)
ProfitLossFormSet = formset_factory(ProfitLossForm, extra=3)
PriceFormSet = formset_factory(PriceForm, extra=3)
StockInFormSet = formset_factory(StockInForm, extra=3)
UserFormSet = formset_factory(UserForm, extra=3)
ProfileFormSet = formset_factory(ProfileForm, extra=3)
