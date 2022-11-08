from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import generic as views
from django.views.generic import TemplateView
from .models import Task
from .forms import AddTask, RegisterForm
from django.views import generic as gen_views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

class HomeView(views.TemplateView):
    template_name = 'tasks/home.html'


class TaskView(views.ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    ordering = 'task_date', 'created_at'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TaskCompletedView(views.ListView):
    model = Task
    template_name = 'tasks/completed-tasks.html'
    ordering = 'task_date', 'created_at'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddTaskView(PermissionRequiredMixin, views.FormView):
    permission_required = ('is_active',)
    template_name = 'tasks/add-task.html'
    form_class = AddTask
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class EditTaskView(PermissionRequiredMixin, views.UpdateView):
    permission_required = ()
    model = Task
    form_class = AddTask
    template_name = 'tasks/add-task.html'
    success_url = '/tasks/'


class DeleteTaskView(PermissionRequiredMixin, views.DeleteView):
    permission_required = ()
    model = Task
    template_name = 'tasks/tasks-confirm-delete.html'
    success_url = '/tasks/'


class TaskDetailView(TemplateView):
    template_name = 'tasks/task-details.html'

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        gymnast = get_object_or_404(Task, **kwargs)
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
    success_url = reverse_lazy('login page')
    template_name = 'profile/register.html'


class UserLoginView(auth_views.LoginView):
    template_name = 'profile/login.html'
    success_url = reverse_lazy('show index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()