# apps/product/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product-index'),
]
