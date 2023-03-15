from django import forms

from .models import Item


class NewItemForm(form.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description','price','image',)