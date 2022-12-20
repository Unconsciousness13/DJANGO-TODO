from django.contrib import admin
from .models import Task, CustomUser
from django.contrib.auth.admin import UserAdmin
# from django.forms import Textarea

@admin.register(Task)
class GymnastAdminConfig(admin.ModelAdmin):
    search_fields = ('task_date', 'user', 'title')
    list_filter = ('task_date', 'user', 'title')
    ordering = ('id',)
    list_display = ( 'id' ,'user', 'title', 'description', 'task_date', 'task_hour' , 'completed' , 'created_at')

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'last_name')
    list_filter = ('email', 'user_name', 'groups')
    ordering = ('id',)
    list_display = ('email', 'user_name', 'first_name', 'last_name', 'is_active', 'is_staff',)

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'is_superuser' , 'user_permissions')}),
        
    )



    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )


admin.site.register(CustomUser, UserAdminConfig)
