from django.urls import path
from about import views

app_name = 'about'

about_template_path = 'about/index.html'
urlpatterns = [
    path('', views.description, name='description'),
]
