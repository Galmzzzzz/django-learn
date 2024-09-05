from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('mews/', include('mews.urls')),
    path('mews', RedirectView.as_view(url='/mews/', permanent=True)),
    path('user/', include('users.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
