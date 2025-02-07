from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.index, name='index'),
#     path('save/',views.save, name="save"),
#     path("add-food/",views.add_food,name="add-food"),
#     # path('delete/<int:id>/',views.delete,name="delete"),
#     # path('edit/<int:id>/',views.edit,name="edit"),
#     # path('edit/edit-food/<int:id>/',views.editf,name="editf")
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('add-food/',views.add_food,name="add_food"),
    path("add-food-form/",views.add_food_form,name="add_food_form"),
    path('add-gadget/',views.add_gadget,name="add_gadget"),
    path("add-gadget-form/",views.add_gadget_form,name="add_gadget_form"),
    path('delete-food/<int:id>/',views.delete_food,name="delete_food"),
    path('delete-gadget/<int:id>/',views.delete_gadget,name="delete_gadget"),
    path('edit-food/<int:id>/',views.edit_food,name="edit_food"),
    path('edit-food-form/<int:id>/',views.edit_food_form,name="edit_food_form"),
    path('edit-gadget/<int:id>/',views.edit_gadget,name="edit_gadget"),
    path('edit-gadget/edit-gadget-form/<int:id>/',views.edit_gadget_form,name="edit_gadget_form")
]