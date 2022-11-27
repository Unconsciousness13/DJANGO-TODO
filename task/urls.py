from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy


urlpatterns = [
    path('', views.HomeView.as_view(), name='show_index'),
    path('login/', views.UserLoginView.as_view(), name='login_page'),
    path('register/', views.UserRegisterView.as_view(), name='register_page'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login_page')), name='logout'),
    path('addtask/', views.AddTaskView.as_view(), name='add_task'),
    path('tasks/', views.TaskView.as_view(), name='tasks_view'),
    path('task/edit/<int:pk>/', views.EditTaskView.as_view(), name='task_edit'),
    path('task/delete/<int:pk>/', views.DeleteTaskView.as_view(), name='task_delete'),
    path('task-completed/' , views.TaskCompletedView.as_view(), name='tasks_completed_view'),
    # ES
    
    path('login-es/', views.UserLoginViewEs.as_view(), name='login_page_es'),
    path('register-es/', views.UserRegisterViewEs.as_view(), name='register_page_es'),
    path('logout-es/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login_page_es')), name='logout_es'),
    path('home-es/', views.HomeViewEs.as_view(), name='show_index_es'),
    path('addtask-es/', views.AddTaskViewEs.as_view(), name='add_task_es'),
    path('tasks-es/', views.TaskViewEs.as_view(), name='tasks_view_es'),
    path('task-es/edit/<int:pk>/', views.EditTaskViewEs.as_view(), name='task_edit_es'),
    path('task-es/delete/<int:pk>/', views.DeleteTaskViewEs.as_view(), name='task_delete_es'),
    path('task-completed-es/' , views.TaskCompletedViewEs.as_view(), name='tasks_completed_view_es'),
    # BG
    path('login-bg/', views.UserLoginViewBg.as_view(), name='login_page_bg'),
    path('register-bg/', views.UserRegisterViewBg.as_view(), name='register_page_bg'),
    path('logout-bg/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login_page_bg')), name='logout_bg'),
    path('home-bg/', views.HomeViewBg.as_view(), name='show_index_bg'),
    path('addtask-bg/', views.AddTaskViewBg.as_view(), name='add_task_bg'),
    path('tasks-bg/', views.TaskViewBg.as_view(), name='tasks_view_bg'),
    path('task-bg/edit/<int:pk>/', views.EditTaskViewBg.as_view(), name='task_edit_bg'),
    path('task-bg/delete/<int:pk>/', views.DeleteTaskViewBg.as_view(), name='task_delete_bg'),
    path('task-completed-bg/' , views.TaskCompletedViewBg.as_view(), name='tasks_completed_view_bg'),
    
    
    #ProfileViews
#     path('create-grpoup/' , views.AddGroupView.as_view() , name='create_group'),
    
    
    path('profile/', views.ProfilePageView.as_view(), name='profile_view'),
    path('profile-edit/<int:pk>/', views.profile_edit, name='profile_edit'),
    #passwords reset delete user , etc.
     path('profile-delete/<int:pk>', views.DeleteProfileView.as_view(), name="profile_delete"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='profile/password-reset.html'),
         name="password_reset"),

    path('password_reset_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='profile/password-reset-sent.html'),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='profile/password-reset-form.html'),
         name="password_reset_confirm"),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='profile/password-reset-complete.html'),
         name="password_reset_complete"),


] 
