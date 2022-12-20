from django.contrib import admin
from .models import FriendList,FriendRequest,UsersGroup
# Register your models here.
class FriendListAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display= ['user']
    search_fields= ['user']
    class Meta:
        model = FriendList
 
 
class FriendRequestAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'reciever']
    list_display= ['sender', 'reciever']
    search_fields= ['sender', 'reciever']
    class Meta:
        model = FriendRequest

admin.site.register(FriendRequest, FriendRequestAdmin)      
admin.site.register(FriendList, FriendListAdmin)
admin.site.register(UsersGroup)