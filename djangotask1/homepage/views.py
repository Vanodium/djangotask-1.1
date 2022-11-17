from django.shortcuts import render
from catalog.models import Item


def home(request):
    items = Item.objects.all().filter(is_published=True, is_on_main=False)
    context = {'items': items, 'navbar': 'home'}
    return render(request, 'homepage/index.html', context)
