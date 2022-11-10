from django.urls import path
from .views import HomeView, UserRegisterView, UserLoginView , AddTaskView ,TaskView , EditTaskView , DeleteTaskView , TaskCompletedView
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy


urlpatterns = [
    path('', HomeView.as_view(), name='show index'),
    path('login/', UserLoginView.as_view(), name='login_page'),
    path('register/', UserRegisterView.as_view(), name='register_page'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('show index')), name='logout'),
    path('addtask/', AddTaskView.as_view(), name='add_task'),
    path('tasks/', TaskView.as_view(), name='tasks_view'),
    path('task/edit/<int:pk>/', EditTaskView.as_view(), name='task_edit'),
    path('task/delete/<int:pk>/', DeleteTaskView.as_view(), name='task_delete'),
    path('task-completed/' , TaskCompletedView.as_view(), name='tasks_completed_view'),
] 
