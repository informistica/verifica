from django.urls import path
from .views import listaArticoliView,listaGiornalistiView
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.home, name='home'),
    path('lista-giornalisti',  listaGiornalistiView.as_view(), name='lista_giornalisti'),
    path('lista-articoli', listaArticoliView.as_view(), name='lista_articoli'),
]
