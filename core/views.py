from django.shortcuts import render
from item.models import Category,Items
from .forms import SignupForm

# Create your views here.
def index(request):
    items = Items.objects.filter(is_sold=False)
    categories = Category.objects.all()
    context = {'items':items, 'categories':categories}
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form =  SignupForm
    context = {'form':form}
    return render(request, 'core/signup.html')