from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('registration/', views.CreateUserView.as_view(), name='registration'),
    path('user/<int:pk>/', views.UserUpdateView.as_view(), name='update_user'),
    path('user/delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete_user'),
]