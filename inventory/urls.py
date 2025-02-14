from django.urls import path
from .views import (
    TableAndItemView, TableCreateView, ItemCreateView, ItemUpdateView, ItemDeleteView
)

urlpatterns = [
    path("", TableAndItemView.as_view(), name="home"),
    path("tables/new/", TableCreateView.as_view(), name="table_create"),
    path("tables/<int:table_id>/items/add/",
         ItemCreateView.as_view(), name="item_create"),
    path("items/<int:pk>/edit/", ItemUpdateView.as_view(), name="item_update"),
    path("items/<int:pk>/delete/",
         ItemDeleteView.as_view(), name="item_delete"),
]
