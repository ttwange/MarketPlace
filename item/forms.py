from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Items


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('category', 'name','description','price','image')
