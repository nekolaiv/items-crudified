from django.urls import path
from .views import (
    TableAndItemView, TableCreateView, ItemCreateView, ItemUpdateView, ItemDeleteView, TableDeleteView, TableUpdateView
)

urlpatterns = [
    path("", TableAndItemView.as_view(), name="table_view"),
    path("tables/new/", TableCreateView.as_view(), name="table_create"),
    path("tables/<int:pk>/table/edit/",
         TableUpdateView.as_view(), name="table_update"),
    path("tables/<int:pk>/table/delete/",
         TableDeleteView.as_view(), name="table_delete"),
    path("tables/<int:table_id>/items/add/",

         ItemCreateView.as_view(), name="item_create"),
    path("tables/<int:table_id>/items/<int:pk>/edit/",
         ItemUpdateView.as_view(), name="item_update"),
    path("tables/<int:table_id>/items/<int:pk>/delete/",
         ItemDeleteView.as_view(), name="item_delete"),
]
