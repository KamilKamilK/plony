from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import UpdateView, CreateView


class CreateUserView(LoginRequiredMixin,CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'obj_list_employee.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': User.objects.all()})
        return context

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    fields = ['last_login','username', 'first_name', 'last_name','email','date_joined']
    success_url = "/"
    template_name = 'obj_list_employee.html'

class UserDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return render(request,"delete_view.html", {'user': user})

    def post(self, request, pk):

        if request.POST['delete'] == 'Tak':
            User.objects.get(pk=pk).delete()
            return redirect(reverse('registration'))
