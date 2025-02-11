from django.urls import path
from .views import FoodCreateView, FoodUpdateView, FoodDeleteView, HomeListView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('food/add/', FoodCreateView.as_view(), name='add_food'),
    path('food/edit/<int:pk>/', FoodUpdateView.as_view(), name='edit_food'),
    path('food/delete/<int:pk>/', FoodDeleteView.as_view(), name='food_delete'),
]
