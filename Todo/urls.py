from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),
    path('groups/', include ('groups.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'task.views.handler404'
handler500 = 'task.views.handler500'