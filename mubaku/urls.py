from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from website import views, admin

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('', views.home, name='home'),
    path('services/', include('services.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
