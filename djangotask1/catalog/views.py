from django.shortcuts import render
from catalog.models import Item
from django.shortcuts import get_object_or_404


def item_list(request):
    items = Item.objects.filter(is_published=True).order_by('category')
    context = {'items': items, 'navbar': 'catalog'}
    return render(request, 'catalog/index.html', context)


def item_detail(request, pk: int):
    item = get_object_or_404(Item, pk=pk)
    context = {'item': item, 'navbar': 'catalog'}
    return render(request, 'catalog/detail.html', context)
