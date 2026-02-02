from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('recepti/', views.RecipeListView.as_view(), name='recipe-list'),
    path('recept/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recept/novi/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recept/<int:pk>/uredi/', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('recept/<int:pk>/obrisi/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
    path('savjeti/', views.TipListView.as_view(), name='tip-list'),
]
