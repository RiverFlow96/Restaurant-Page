from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions

from apps.restaurant.home_views import api_home, api_docs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_home, name='api-home'),
    path('api/', api_home, name='api-root'),
    path('api/docs/', api_docs, name='api-docs'),
    path('api/v1/restaurant/', include('apps.restaurant.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)