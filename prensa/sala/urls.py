from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('agenda/', views.calendario, name='calendario'),
    path('login/', views.login_view, name='login'), # Esta se queda por si acaso
    path('logout/', views.logout_view, name='logout'),
    path('agenda/nuevo/', views.crear_evento, name='crear_evento'),
    path('registro-medio/', views.registro_medio, name='registro_medio'),
    path('activar-cuenta/<int:user_id>/', views.activar_cuenta, name='activar_cuenta'),
    path('agenda/extraer-word/', views.extraer_datos_word, name='extraer_word'),
    path('agenda/descargar-pack/<int:evento_id>/', views.descargar_pack_medios, name='descargar_pack'),
    path('recursos/', views.galeria_recursos, name='recursos'),
]