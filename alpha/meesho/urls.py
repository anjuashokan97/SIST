from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("file", views.file, name='file'),
    path("contact", views.contact, name='contact'),
    path("sign", views.sign, name='sign')
]
