from django import forms
from .models import Food, Gadget

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'price']


class GadgetForm(forms.ModelForm):
    class Meta:
        model = Gadget
        fields = ['name', 'price']
