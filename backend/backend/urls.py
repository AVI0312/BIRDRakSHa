# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Add this line to include the 'api' app's URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
