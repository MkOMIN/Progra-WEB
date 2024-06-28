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
    path('admin/', views.admin , name='admin'),
    path('crud', views.crud, name='crud'),
    path('usuarios_del/<str:pk>', views.usuarios_del, name='usuarios_del'),
    path('usuarios_findEdit/<str:pk>', views.usuarios_findEdit, name='usuarios_findEdit'),
    path('usuariosUpdate', views.usuariosUpdate, name='usuariosUpdate'),
    
    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd', views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),
    
    path('menu', views.menu, name='menu'),
]
