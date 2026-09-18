from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
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

# Configuración para servir archivos multimedia en local y producción (Railway/Gunicorn)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)