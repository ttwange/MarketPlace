from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Items
from .forms import NewItemForm, EditItemForm

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Items, pk=pk)
    related_items = Items.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    context = {"item": item, 'related_items':related_items}
    return render(request, 'item/detail.html',context)

@login_required
def edit(request):
    item = get_object_or_404(Items, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm()
    context = {'form':form, 'title': 'Edit item'}
    return render(request, 'item/form.html', context)

@login_required
def delete(request,pk):
    item = get_object_or_404(Items, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')