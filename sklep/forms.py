from django import forms
from sklep.models import Category, Product, Employee, Season, Company




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['slug']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['slug']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        exclude = ['slug']
        widgets = {
            'products': forms.CheckboxSelectMultiple,
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['slug']