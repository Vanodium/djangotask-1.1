from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Item


def item_list(request):
    items = Item.objects.all()
    context = {
        'items': items,
        'navbar': 'catalog'
    }
    return render(request, 'catalog/index.html', context)


def item_detail(request, pk: int):
    return HttpResponse(f'Подробно элемент №{pk}')
