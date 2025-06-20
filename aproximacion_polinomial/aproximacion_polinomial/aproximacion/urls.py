from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('interpolacion/', views.interpolacion_view, name='interpolacion'),
    path('interpolacion_inversa/', views.interpolacion_inversa_view, name='interpolacion_inversa'),

]

    