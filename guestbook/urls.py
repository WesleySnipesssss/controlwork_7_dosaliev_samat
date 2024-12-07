from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_list, name='entry_list'),
    path('add/', views.entry_add, name='entry_add'),
    path('edit/<int:pk>/', views.entry_edit, name='entry_edit'),
    path('delete/<int:pk>/', views.entry_delete, name='entry_delete'),
]
