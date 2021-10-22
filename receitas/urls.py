from django.urls import path #importando as urls do django
from . import views #importando todas as views, views manipula qual urls queremos mostra

urlpatterns = [
    path('',views.index, name="index") #primeiro parãmetro e a rota, a segunda ea view responsavel por essa rota, namespace para as entradas urls
]