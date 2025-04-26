from django.urls import path
from . import views

urlpatterns = [
    path('', views.code_list, name='code_list'),
    path('create/', views.code_create, name='code_create'),
    path('edit/<int:pk>/', views.code_update, name='code_update'),
    path('delete/<int:pk>/', views.code_delete, name='code_delete'),
]
