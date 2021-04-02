from django.urls import path

from . import views

app_name = 'elecciones'

urlpatterns = [
    # ex: /elecciones/
    path('', views.index, name='index'),
    # ex: /elecciones/#/
    path('<int:region_id>/', views.detalle, name='detalle'),
    # ex: /elecciones/#/resultados/
    path('<int:region_id>/resultados/', views.resultados, name='resultados'),
    # ex: /elecciones/#/voto/
    path('<int:region_id>/voto/', views.votar, name='votar'),
]