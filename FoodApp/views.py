from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.generic import ListView

from FoodApp.forms import ItemForm
from FoodApp.models import Item

# Home view: Display all items correctly
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})  # Fixed context key to 'items'

# class IndexView(ListView):
#     model = Item
#     templates_name = 'home.html'
#     context_object_name = 'items'
#






# Detail view: Fetch a single item by ID and search functionality
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)  # Safer approach for item lookup
    query = request.GET.get('q')
    if query:
        items = Item.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        items = Item.objects.all()
    return render(request, 'detail.html', {'item': item, 'items': items})  # Fixed context keys

# Create Item view: Form handling for adding a new item
from django.shortcuts import render, redirect
from .forms import ItemForm

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'add.html', {'form': form})


def update_product(request,id):
    item = get_object_or_404(Item, id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'add.html', {'form': form})





def delete_product(request, id):
    # Get the product object by its id
    product = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('home')  # Redirect to home or any other page

    return render(request, 'delete.html', {'product': product})