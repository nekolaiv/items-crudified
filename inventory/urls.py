from django.urls import path
from .views import FoodCreateView, FoodUpdateView, FoodDeleteView, GadgetCreateView, GadgetDeleteView, GadgetUpdateView, HomeListView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('food/add', FoodCreateView.as_view(), name='add_food'),
    path('gadget/add', GadgetCreateView.as_view(), name='add_gadget'),
    path('food/edit/<int:pk>/', FoodUpdateView.as_view(), name='edit_food'),
    path('gadget/edit/<int:pk>/', GadgetUpdateView.as_view(), name='edit_food'),
    path('food/delete/<int:pk>/', FoodDeleteView.as_view(), name='food_delete'),
    path('gadget/delete/<int:pk>/',
         GadgetDeleteView.as_view(), name='gadget_delete'),
]
