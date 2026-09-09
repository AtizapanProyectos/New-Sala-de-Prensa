from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-agent: AdsBot-Google",
        "Allow: /",
        "",
        "User-agent: Googlebot",
        "Allow: /",
        "",
        "User-agent: *",
        "Allow: /",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain; charset=utf-8")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', robots_txt, name='robots_txt'),
    # Aquí llamamos a las urls de la app
    path('', include('sala.urls')), 
]

# Configuración necesaria para servir tus archivos estáticos y media
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)