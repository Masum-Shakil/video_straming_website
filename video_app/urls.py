from django.contrib import admin
from django.urls import path, include
from .views import index, details, ajax_search

urlpatterns = [
    path('', index, name='index'),
    path('details/<int:id>', details, name='details'),
    path('search/', ajax_search, name='search')
]