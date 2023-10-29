from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # http://localhost:8000/admin/
    path('admin/', admin.site.urls),

    # http://localhost:8000/
    path('', include('app_main.urls')),

    # http://localhost:8000/profiles/
    path('profiles/', include('app_users.urls'))
]

urlpatterns += static(prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
