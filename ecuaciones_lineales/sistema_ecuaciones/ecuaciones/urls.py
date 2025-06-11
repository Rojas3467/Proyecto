from django.urls import path
from . import views

urlpatterns = [
    path('', views.resolver_sistema, name='resolver_sistema'),
]
