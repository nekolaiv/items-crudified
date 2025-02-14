from django.urls import path
from .views import (
    TableListView, TableCreateView, TableDetailView, TableDeleteView,
    ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView
)

urlpatterns = [
    # Table URLs
    path("", TableListView.as_view(), name="table_list"),
    path("tables/new/", TableCreateView.as_view(), name="table_create"),
    path("tables/<int:pk>/", TableDetailView.as_view(), name="table_detail"),
    path("tables/<int:pk>/delete/", TableDeleteView.as_view(), name="table_delete"),

    # Item URLs (inside a table)
    path("tables/<int:table_id>/items/",
         ItemListView.as_view(), name="item_list"),
    path("tables/<int:table_id>/items/new/",
         ItemCreateView.as_view(), name="item_create"),
    path("items/<int:pk>/edit/", ItemUpdateView.as_view(), name="item_update"),
    path("items/<int:pk>/delete/", ItemDeleteView.as_view(), name="item_delete"),
]
