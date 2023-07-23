from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Items

# Create your views here.
@login_required
def index(request):
    item = Items.objects.filer(created_by = request.user)
    context = {'item':item}
    return render(request, 'dashboard/index.html', context)