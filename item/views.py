from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Items
from .forms import NewItemForm,EditItemForm

# Create your views here.
def items(request):
    query = request.GET.get('query','')
    items = Items.objects.filter(is_sold=False)
    if query:
        items = items.filter(name__icontains = query)
    context = {'items':items,'query':query}
    return render(request,'item/items.html',context)


def detail(request, pk):
    item = get_object_or_404(Items, pk=pk)
    related_items = Items.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    context = {"item": item, 'related_items':related_items}
    return render(request, 'item/detail.html',context)

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    context = {'form':form, 'title': 'New item'}
    return render(request, 'item/form.html', context)

@login_required
def edit(request, pk):
    item = get_object_or_404(Items, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    context = {'form':form, 'title': 'Edit item'}
    return render(request, 'item/form.html', context)

@login_required
def delete(request,pk):
    item = get_object_or_404(Items, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard')