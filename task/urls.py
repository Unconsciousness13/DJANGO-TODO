from django.urls import path
from .views import HomeView, UserRegisterView, UserLoginView
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy


urlpatterns = [
    path('', HomeView.as_view(), name='show index'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('register/', UserRegisterView.as_view(), name='register page'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('show index')), name='logout'),

    
] 
