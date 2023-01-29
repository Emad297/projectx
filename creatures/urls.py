from django.urls import path
from . import views

urlpatterns = [
    path('', views.creature_list, name='creature_list'),
    path('new/', views.creature_create, name='creature_create'),
    path('update/<int:pk>/', views.creature_update, name='creature_update'),
    path('delete/<int:pk>/', views.creature_delete, name='creature_delete'),
]