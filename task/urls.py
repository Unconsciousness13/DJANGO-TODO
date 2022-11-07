from django.urls import path, include
from django.conf.urls.static import static
from .views import HomeView


from django.conf import settings


urlpatterns = [
    path('', HomeView.as_view(), name='show index'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
