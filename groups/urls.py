from django.urls import path
from . import views

urlpatterns = [
    path('create-group/' , views.AddGroupView.as_view() , name='create_group'),
    path('friends/' , views.friends_list_view , name='friends list'),
    path('groups/' , views.groups_list_view , name='groups list'),
]

