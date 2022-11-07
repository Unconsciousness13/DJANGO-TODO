from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import generic as views
from django.views.generic import TemplateView
from .models import Task
from .forms import AddTask

class HomeView(views.TemplateView):
    template_name = 'tasks/home.html'


class TaskView(views.ListView):
    model = Task
    template_name = 'tasks/task.html'
    ordering = 'task_date', 'created_at'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddTaskView(PermissionRequiredMixin, views.FormView):
    permission_required = ()
    template_name = 'tasks/add-task.html'
    form_class = Task
    success_url = '/tasks/'

    def form_valid(self, form):
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
