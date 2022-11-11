from django.urls import path
from homepage import views

app_name = 'homepage'

home_template_path = 'homepage/index.html'
urlpatterns = [
    path('', views.home, name='home')
]
