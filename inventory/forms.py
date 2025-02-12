from django import forms
from .models import Food, Table


class Table(forms.ModelForm):
    class Meta:
        model = Table
        fields = ["name"]


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400',
                'placeholder': 'Enter food name...'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400',
                'placeholder': 'Enter price...'
            }),
        }
