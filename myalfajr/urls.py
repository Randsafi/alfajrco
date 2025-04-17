from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagehome, name='home'),
    path('product/search/', views.search, name='search'),
    path('product/search/', views.search_e, name='search_e'),
    path('product/<str:category>/', views.product, name='product'),
   # path('search/', views.search_product, name='search_product'),  # جديد للبحث
]
   
