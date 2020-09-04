from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from sklep import views

urlpatterns = [
                  path('', views.IndexView.as_view(), name='main'),
                  path('management/', views.ManagementView.as_view(), name='plony-management'),
                  path('accounts/', include('accounts.urls')),

                  path('categories/', views.CategoryView.as_view(), name='categories'),
                  path('categories/create', views.CategoryCreateView.as_view(), name='create_category'),
                  path('category/delete/<int:pk>', views.CategoryDeleteView.as_view(), name='delete_category'),
                  path('category/<str:slug>', views.CategoryUpdateView.as_view(), name='update_category'),
                  path('categories/<str:slug>', views.ProductsCategoryView.as_view(), name='products_cat_list'),

                  path('product/<str:slug>', views.ProductView.as_view(), name='product'),
                  path('product/create/', views.ProductCreateView.as_view(), name='create_product'),
                  path('product/delete/<int:pk>', views.ProductDeleteView.as_view(), name='delete_product'),
                  path('products/<str:slug>', views.ProductUpdateView.as_view(), name='update_product'),

                  path('employees', views.EmployeeView.as_view(), name='employees'),
                  path('employee/create', views.EmployeeCreateView.as_view(), name='create_employee'),
                  path('employee/delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='delete_employee'),
                  path('employee/<int:pk>', views.EmployeeUpdateView.as_view(), name='update_employee'),

                  path('season/<str:slug>', views.SeasonDetailView.as_view(), name='season'),
                  path('season/create/', views.SeasonCreateView.as_view(), name='create_season'),
                  path('season/delete/<int:pk>', views.SeasonDeleteView.as_view(), name='delete_season'),
                  path('seasons/<str:slug>', views.SeasonUpdateView.as_view(), name='update_season'),

                  path('company/<str:slug>', views.CompanyView.as_view(), name='company'),
                  path('company/create/', views.CompanyCreateView.as_view(), name='create_company'),
                  path('company/delete/<int:pk>', views.CompanyDeleteView.as_view(), name='delete_company'),
                  path('companies/<str:slug>', views.CompanyUpdateView.as_view(), name='update_company'),



              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)