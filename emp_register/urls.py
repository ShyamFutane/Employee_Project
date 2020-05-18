from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.emp_form, name='emp_add'),  # for adding new employee record.
    path('<int:id>/', views.emp_form, name='emp_update'),  # for modification of existing employee record.
    path('delete/<int:id>/', views.emp_delete, name='emp_delete'),  # for modification of existing employee record.
    path('list/', views.emp_list, name='emp_list')  # for deleting respective employee record.
]
