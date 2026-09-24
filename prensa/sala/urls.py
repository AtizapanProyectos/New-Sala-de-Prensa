from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('agenda/', views.calendario, name='calendario'),
    path('login/', views.login_view, name='login'), # Esta se queda por si acaso
    path('logout/', views.logout_view, name='logout'),
    path('agenda/nuevo/', views.crear_evento, name='crear_evento'),
    path('agenda/carga-masiva/', views.carga_masiva_boletines, name='carga_masiva'),
    path('agenda/carga-masiva/procesar/', views.procesar_boletin_individual, name='procesar_boletin_individual'),
    path('registro-medio/', views.registro_medio, name='registro_medio'),
    path('activar-cuenta/<int:user_id>/', views.activar_cuenta, name='activar_cuenta'),
    path('agenda/extraer-word/', views.extraer_datos_word, name='extraer_word'),
    path('agenda/descargar-pack/<int:evento_id>/', views.descargar_pack_medios, name='descargar_pack'),
    path('recursos/', views.galeria_recursos, name='recursos'),
    # Endpoints Administrativos (Super Admin)
    path('agenda/evento/<int:evento_id>/editar/', views.editar_evento_api, name='editar_evento_api'),
    path('agenda/evento/<int:evento_id>/seleccionar-portada/', views.seleccionar_portada_api, name='seleccionar_portada_api'),
    path('agenda/evento/<int:evento_id>/subir-fotos/', views.subir_foto_galeria_api, name='subir_foto_galeria_api'),
    path('agenda/foto/<int:imagen_id>/eliminar/', views.eliminar_foto_galeria_api, name='eliminar_foto_galeria_api'),
    path('agenda/evento/<int:evento_id>/mover-fecha/', views.mover_fecha_evento_api, name='mover_fecha_evento_api'),
    path('agenda/evento/<int:evento_id>/eliminar/', views.eliminar_evento_api, name='eliminar_evento_api'),
]