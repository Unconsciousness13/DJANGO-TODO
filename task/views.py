from django.contrib.auth.mixins import  LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import generic as views
from django.views.generic import TemplateView
from .models import Task
from .forms import AddTask, RegisterForm
from django.views import generic as gen_views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import redirect_to_login

    


class HomeView(LoginRequiredMixin ,views.ListView):
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'
    model = Task
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count_incompleted'] = context['tasks'].filter(completed=False).count()
        context['count_completed'] = context['tasks'].filter(completed=True).count()
        return context


class TaskView(LoginRequiredMixin ,views.ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    ordering = 'task_date', 'created_at'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count_incompleted'] = context['tasks'].filter(completed=False).count()
        context['count_completed'] = context['tasks'].filter(completed=True).count()
        context['incompleted_tasks'] = context['tasks'].filter(completed=False)
        
        return context

class TaskCompletedView(LoginRequiredMixin,views.ListView):
    model = Task
    template_name = 'tasks/completed-tasks.html'
    ordering = 'task_date', 'created_at'
    context_object_name = 'tasks'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count_incompleted'] = context['tasks'].filter(completed=False).count()
        context['count_completed'] = context['tasks'].filter(completed=True).count()
        context['completed_tasks'] = context['tasks'].filter(completed=True)
        
        return context
            

class AddTaskView(LoginRequiredMixin, views.FormView):
    template_name = 'tasks/add-task.html'
    form_class = AddTask
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class EditTaskView(LoginRequiredMixin, views.UpdateView):
    model = Task
    form_class = AddTask
    template_name = 'tasks/edit-task.html'
    success_url = '/tasks/'
    context_object_name = 'tasks'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    


class DeleteTaskView(LoginRequiredMixin, views.DeleteView):
    model = Task
    template_name = 'tasks/tasks-confirm-delete.html'
    success_url = '/tasks/'
    context_object_name = 'tasks'

    

class TaskDetailView(LoginRequiredMixin,TemplateView):
    template_name = 'tasks/task-details.html'

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        task = get_object_or_404(Task, **kwargs)
        context['user'] = Task.user
        context['title'] = Task.title
        context['description'] = Task.description
        context['task_date'] = Task.task_date
        context['task_hour'] = Task.task_hour
        context['created_at'] = Task.created_at
        context['completed'] = Task.completed

        return context


class UserRegisterView(gen_views.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login_page')
    template_name = 'profile/register.html'


class UserLoginView(auth_views.LoginView):
    template_name = 'profile/login.html'
    success_url = reverse_lazy('show_index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()