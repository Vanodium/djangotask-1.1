from django.shortcuts import render
from homepage import urls


def home(request):
    return render(request, urls.home_template_path)
