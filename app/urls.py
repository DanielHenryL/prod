from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('/', include(('bases.urls','bases'), namespace='bases')),
    path('inv/', include(('inv.urls','inv'), namespace='inv')),
    path('cmp/', include(('cmp.urls','cmp'), namespace='cmp')),
    path('fac/', include(('fac.urls','fac'), namespace='fac')),
    path('api/', include(('api.urls','api'), namespace='api')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
