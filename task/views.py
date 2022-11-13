from django.contrib.auth.mixins import  LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import generic as views
from django.views.generic import TemplateView
from .models import Task
from .forms import AddTask, AddTaskEs, AddTaskBg, RegisterForm ,RegisterFormBg , RegisterFormEs
from django.views import generic as gen_views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.shortcuts import  render

    


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
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['incompleted_tasks'] = context['tasks'].filter(title__icontains = search_input) or context['tasks'].filter(description__icontains = search_input)
            
                   
        context['search_input'] = search_input
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
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['completed_tasks'] = context['tasks'].filter(title__icontains = search_input) or context['tasks'].filter(description__icontains = search_input)
                   
        context['search_input'] = search_input
        
        return context
            

class AddTaskView(LoginRequiredMixin, views.FormView):
    template_name = 'tasks/add-task.html'
    form_class = AddTask
    success_url = '/tasks/'

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
    redirect_authenticated_user = True
    
    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()
    
    
# ES

class HomeViewEs(LoginRequiredMixin ,views.ListView):
    template_name = 'tasks/home-es.html'
    context_object_name = 'tasks'
    model = Task
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count_incompleted'] = context['tasks'].filter(completed=False).count()
        context['count_completed'] = context['tasks'].filter(completed=True).count()
        return context
    
    
class EditTaskViewEs(LoginRequiredMixin, views.UpdateView):
    model = Task
    form_class = AddTaskEs
    template_name = 'tasks/edit-task-es.html'
    success_url = '/tasks/'
    context_object_name = 'tasks'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class TaskViewEs(LoginRequiredMixin ,views.ListView):
    model = Task
    template_name = 'tasks/tasks-es.html'
    ordering = 'task_date', 'created_at'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count_incompleted'] = context['tasks'].filter(completed=False).count()
        context['count_completed'] = context['tasks'].filter(completed=True).count()
        context['incompleted_tasks'] = context['tasks'].filter(completed=False)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['incompleted_tasks'] = context['tasks'].filter(title__icontains = search_input) or context['tasks'].filter(description__icontains = search_input)
            
                   
        context['search_input'] = search_input
        return context

class TaskCompletedViewEs(LoginRequiredMixin,views.ListView):
    model = Task
    template_name = 'tasks/completed-tasks-es.html'
    ordering = 'task_date', 'created_at'
    context_object_name = 'tasks'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count_incompleted'] = context['tasks'].filter(completed=False).count()
        context['count_completed'] = context['tasks'].filter(completed=True).count()
        context['completed_tasks'] = context['tasks'].filter(completed=True)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['completed_tasks'] = context['tasks'].filter(title__icontains = search_input) or context['tasks'].filter(description__icontains = search_input)
                   
        context['search_input'] = search_input
        
        return context
            

class AddTaskViewEs(LoginRequiredMixin, views.FormView):
    template_name = 'tasks/add-task-es.html'
    form_class = AddTaskEs
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class EditTaskViewEs(LoginRequiredMixin, views.UpdateView):
    model = Task
    form_class = AddTaskEs
    template_name = 'tasks/edit-task-es.html'
    success_url = '/tasks/'
    context_object_name = 'tasks'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    


class DeleteTaskViewEs(LoginRequiredMixin, views.DeleteView):
    model = Task
    template_name = 'tasks/tasks-confirm-delete-es.html'
    success_url = '/tasks/'
    context_object_name = 'tasks'


class UserRegisterViewEs(gen_views.CreateView):
    form_class = RegisterFormEs
    success_url = reverse_lazy('login_page_es')
    template_name = 'profile/register-es.html'


class UserLoginViewEs(auth_views.LoginView):
    template_name = 'profile/login-es.html'
    success_url = reverse_lazy('show_index_es')
    redirect_authenticated_user = True
    
    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()



# BG

class HomeViewBg(LoginRequiredMixin ,views.ListView):
    template_name = 'tasks/home-bg.html'
    context_object_name = 'tasks'
    model = Task
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count_incompleted'] = context['tasks'].filter(completed=False).count()
        context['count_completed'] = context['tasks'].filter(completed=True).count()
        return context


class TaskViewBg(LoginRequiredMixin ,views.ListView):
    model = Task
    template_name = 'tasks/tasks-bg.html'
    ordering = 'task_date', 'created_at'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count_incompleted'] = context['tasks'].filter(completed=False).count()
        context['count_completed'] = context['tasks'].filter(completed=True).count()
        context['incompleted_tasks'] = context['tasks'].filter(completed=False)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['incompleted_tasks'] = context['tasks'].filter(title__icontains = search_input) or context['tasks'].filter(description__icontains = search_input)
            
                   
        context['search_input'] = search_input
        return context

class TaskCompletedViewBg(LoginRequiredMixin,views.ListView):
    model = Task
    template_name = 'tasks/completed-tasks-bg.html'
    ordering = 'task_date', 'created_at'
    context_object_name = 'tasks'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count_incompleted'] = context['tasks'].filter(completed=False).count()
        context['count_completed'] = context['tasks'].filter(completed=True).count()
        context['completed_tasks'] = context['tasks'].filter(completed=True)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['completed_tasks'] = context['tasks'].filter(title__icontains = search_input) or context['tasks'].filter(description__icontains = search_input)
                   
        context['search_input'] = search_input
        
        return context
            

class AddTaskViewBg(LoginRequiredMixin, views.FormView):
    template_name = 'tasks/add-task-bg.html'
    form_class = AddTaskBg
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class EditTaskViewBg(LoginRequiredMixin, views.UpdateView):
    model = Task
    form_class = AddTaskBg
    template_name = 'tasks/edit-task-bg.html'
    success_url = '/tasks/'
    context_object_name = 'tasks'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    


class DeleteTaskViewBg(LoginRequiredMixin, views.DeleteView):
    model = Task
    template_name = 'tasks/tasks-confirm-delete-bg.html'
    success_url = '/tasks/'
    context_object_name = 'tasks'

class UserRegisterViewBg(gen_views.CreateView):
    form_class = RegisterFormBg
    success_url = reverse_lazy('login_page_bg')
    template_name = 'profile/register-bg.html'


class UserLoginViewBg(auth_views.LoginView):
    template_name = 'profile/login-bg.html'
    success_url = reverse_lazy('show_index_bg')
    redirect_authenticated_user = True
    
    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()
    
    
    
# // Errors views //
def handler404(request, exception):
    context = {}
    response = render(request, "tasks/not-exist.html", context=context)
    response.status_code = 404
    return response


def handler500(request):
    context = {}
    response = render(request, "tasks/not-exist.html", context=context)
    response.status_code = 500
    return response