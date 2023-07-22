from django.shortcuts import get_object_or_404, render
from .models import Items

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(item, pk=pk)

    return render(request, 'item/detail.html,{
                  "title": item,
    })