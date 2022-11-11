from django.shortcuts import render
from about import urls


def description(request):
    return render(request, urls.about_template_path)
