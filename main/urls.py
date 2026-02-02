from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('recepti/', views.RecipeListView.as_view(), name='recipe-list'),
    path('recept/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
]
