from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Items


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('category', 'name','description','price','image')


        widgets = {
            'category': forms.Select(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }
