from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Items

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Items, pk=pk)
    related_items = Items.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    context = {"item": item, 'related_items':related_items}
    return render(request, 'item/detail.html',context)

@login_required
def new(request):