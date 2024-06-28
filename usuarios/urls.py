from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto , name='contacto',),
    path('contra_olvido/', views.contra_olvido , name='contra_olvido'),
    path('inicio_sesion/', views.inicio_sesion , name='inicio_sesion'),
    path('registro/', views.registro , name='registro'),
    path('trabajo1/', views.trabajo1 , name='trabajo1'),
    path('trabajo2/', views.trabajo2 , name='trabajo2'),
    path('trabajo3/', views.trabajo3 , name='trabajo3'),
    path('trabajos/', views.trabajos , name='trabajos'),
    path('carrito/', views.carrito , name='carrito'),
]
