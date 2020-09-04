from random import shuffle

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from sklep.forms import CategoryForm, ProductForm, SeasonForm, CompanyForm
from sklep.models import Category, Product, Employee, Season, Company


class IndexView(View):
    def get(self, request):
        karuzela = list(Product.objects.all())
        shuffle(karuzela)
        ctx = {
            'karuzela': karuzela,
            'employees': Employee.objects.all(),
            'objects': Season.objects.last().products.all(),
            'season': Season.objects.last(),
            'companies': Company.objects.all(),
        }
        return render(request, "main.html", ctx)


class ManagementView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'management.html')


class CategoryView(View):
    def get(self, request):
        ctx = {
            'objects': Category.objects.all()
        }
        return render(request, 'category.html', ctx)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('create_category')
    template_name = 'detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': Category.objects.all()})
        return context


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('create_category')
    template_name = 'detail_view.html'


class CategoryDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        return render(request, 'delete_view.html', {'object': category})

    def post(self, request, pk):
        if request.POST['delete'] == 'Tak':
            Category.objects.get(pk=pk).delete()
        return redirect(reverse('create_category'))


class ProductsCategoryView(View):
    def get(self, request, slug):
        category = Category.objects.filter(slug=slug)
        products = Product.objects.filter(categories=category.first())
        ctx = {
            'objects': products,
            'category': category
        }
        return render(request, 'products.html', ctx)

class ProductView(View):
    def get(self, request, slug):
        product = Product.objects.filter(slug=slug)
        ctx = {
            'product': product
        }
        return render(request, 'productView.html', ctx)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('create_product')
    template_name = 'detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': Product.objects.all()})
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('create_product')
    template_name = 'detail_view.html'


class ProductDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'delete_view.html', {'object': product})

    def post(self, request, pk):
        if request.POST['delete'] == 'Tak':
            Product.objects.get(pk=pk).delete()
        return redirect(reverse('create_product'))


class EmployeeView(View):
    def get(self, request):
        ctx = {
            'employees': Employee.objects.all()
        }
        return render(request, 'employees.html', ctx)


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('create_employee')
    template_name = 'detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': Employee.objects.all()})
        return context


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('create_employee')
    template_name = 'detail_view.html'


class EmployeeDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        return render(request, 'delete_view.html', {'object': employee})

    def post(self, request, pk):
        if request.POST['delete'] == 'Tak':
            Employee.objects.get(pk=pk).delete()
        return redirect(reverse('create_employee'))


class SeasonDetailView(View):
    def get(self, request, slug):
        season = Season.objects.get(slug=slug)
        season_products = Season.objects.get(slug=slug).products.all()
        products = Product.objects.all()
        name = request.GET.get('name')
        if name:
            products = products.filter(name__icontains=name)

        ctx = {
            'season_products': season_products,
            'season': season,
            'objects': products,
        }
        return render(request, 'seasons.html', ctx)

    def post(self, request, slug):
        season = Season.objects.get(slug=slug)

        if request.POST['action'] == 'add':
            product = request.POST['product']

            season.products.add(product)
            return redirect(f"/plony/season/{season.slug}")

        elif request.POST['action'] == 'delete':
            product = request.POST['product']

            season.products.remove(product)
            return redirect(f"/plony/season/{season.slug}")

class SeasonCreateView(LoginRequiredMixin, CreateView):
    model = Season
    form_class = SeasonForm
    success_url = reverse_lazy('create_season')
    template_name = 'detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': Season.objects.all()})
        return context


class SeasonUpdateView(LoginRequiredMixin, UpdateView):
    model = Season
    form_class = SeasonForm
    success_url = reverse_lazy('create_season')
    template_name = 'detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': Season.objects.filter(slug=self)})
        return context


class SeasonDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        season = Season.objects.get(pk=pk)
        return render(request, 'delete_view.html', {'object': season})

    def post(self, request, pk):
        if request.POST['delete'] == 'Tak':
            Season.objects.get(pk=pk).delete()
        return redirect(reverse('create_season'))

class CompanyView(View):
    def get(self, request, slug):
        company = Company.objects.filter(slug=slug)
        ctx = {
            'company': company
        }
        return render(request, 'company_view.html', ctx)

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('create_company')
    template_name = 'detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': Company.objects.all()})
        return context

class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('create_company')
    template_name = 'detail_view.html'

class CompanyDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        return render(request, 'delete_view.html', {'object': company})

    def post(self, request, pk):
        if request.POST['delete'] == 'Tak':
            Company.objects.get(pk=pk).delete()
        return redirect(reverse('create_company'))