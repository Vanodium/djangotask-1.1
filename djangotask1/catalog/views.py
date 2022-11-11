from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Item
from catalog import urls


def item_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, urls.catalog_template_path, context)


def item_detail(request, pk: int):
    return HttpResponse(f'Подробно элемент №{pk}')
