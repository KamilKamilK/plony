from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

def stock_validate(value):
    if value <= 0:
        raise ValidationError(' Produkt cały wyprzedany')

def minus_number_validate(value):
    if value <= -1:
        raise ValidationError('Nie można wstawić ujemnej wartości')

class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa', unique=True, null=False)
    description = models.CharField(max_length=128, verbose_name='Przypis', null=True)
    slug = models.SlugField(max_length=64, null=False )
    img = models.ImageField(upload_to='category', verbose_name='Obrazek', null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_detail_url(self):
        return f'plony/categories/{self.slug}'

    def get_update(self):
        return f'plony/category/{self.slug}'

    def get_delete(self):
        return reverse('delete_category', args=(self.pk,))

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa', unique=True, null=False)
    description = models.TextField(verbose_name='Opis', null=True)
    small_description = models.CharField(max_length=64, verbose_name='Przypis', null=True)
    price = models.FloatField(verbose_name='Cena', validators=[minus_number_validate], null=False)
    vat = models.FloatField(verbose_name='Vat', validators=[minus_number_validate], null=True)
    stock = models.PositiveIntegerField(verbose_name='Ilość', validators=[stock_validate], null=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=64, null=False)
    img = models.ImageField(upload_to='products', verbose_name='Obrazek', null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_detail_url(self):
        return f'plony/product/{self.slug}'

    def get_delete(self):
        return reverse('delete_product', args=(self.pk,))

    def get_category(self):
        return f' Kategoria: {self.categories.name}'

    def get_update(self):
        return f'plony/products/{self.slug}'

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Imię',null=False)
    last_name = models.CharField(max_length=64, verbose_name='Nazwisko', null=False)
    occupation = models.CharField(max_length=64, verbose_name='Stanowisko',null=True)
    img = models.ImageField(upload_to='team', verbose_name='Zdjęcie', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='', verbose_name= 'Wybiesz konto', null=True)
    
    def get_detail_url(self):
        return f'plony/employee/{self.pk}'

    def get_delete(self):
        return reverse('delete_employee', args=(self.pk,))

    def get_occupation(self):
        return self.occupation

    def get_update(self):
        return f'plony/employee/{self.pk}'

    def get_account_details(self):
        return f'accounts/user/{self.user_id}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Season(models.Model):
    name = models.CharField(max_length=64, default='', verbose_name='Nazwa', unique=True)
    slug = models.SlugField(max_length=64, default='',null=False)
    description = models.TextField(verbose_name='Opis', default='',null=True)
    img = models.ImageField(upload_to='season', verbose_name='Obrazek', null=False)
    products = models.ManyToManyField(Product)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Season, self).save(*args, **kwargs)

    def get_detail_url(self):
        return f'plony/season/{self.slug}'

    def get_delete(self):
        return reverse('delete_season', args=(self.pk,))

    def get_update(self):
        return f'plony/seasons/{self.slug}'

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa', null=False)
    description = models.CharField(max_length=128, verbose_name='Krótki opis',null=True)
    slug = models.SlugField(max_length=64, null=False)
    img = models.ImageField(upload_to='company', verbose_name='Obrazek', null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)

    def get_detail_url(self):
        return f'plony/company/{self.slug}'

    def get_delete(self):
        return reverse('delete_company', args=(self.pk,))

    def get_update(self):
        return f'plony/companies/{self.slug}'

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=64)
    mail = models.CharField(max_length=64)
    telephone = models.IntegerField()
    message = models.TextField()
