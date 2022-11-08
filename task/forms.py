from django import forms
from .models import Task
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'task_date', 'task_hour',  'completed', )
        labels = {
            'title': 'title',
            'description': 'description',
            'task_date': 'Date of task',
            'task_hour': 'Hour of task',
            'completed': 'is completed?',
        }
        
                



from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('user_name',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',)


class UpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('user_name',
                  'first_name',
                  'last_name',
                  'email',
                  )