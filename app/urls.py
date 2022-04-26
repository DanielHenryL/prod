from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('bases.urls','bases'), namespace='bases')),
    path('inv/', include(('inv.urls','inv'), namespace='inv')),
    path('cmp/', include(('cmp.urls','cmp'), namespace='cmp')),
    path('admin/', admin.site.urls),
]
