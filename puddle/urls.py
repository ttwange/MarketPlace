from django.contrib import admin
from django.urls import path,include
from core.views import index, contact
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('items/', include('item.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
