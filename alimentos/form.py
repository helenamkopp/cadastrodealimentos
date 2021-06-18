from django import forms
from .models import Food


class BoletosForms(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'brand', 'section', 'content', 'price']