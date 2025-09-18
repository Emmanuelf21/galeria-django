from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('galeria/<int:id>/', views.pais_detail, name='pais_detail'),
    path('pesquisa/', views.pesquisar_pais, name='pesquisar_pais'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('contato/', views.contato, name='contato'),
    path('sucesso', views.sucesso, name='sucesso'),
]

