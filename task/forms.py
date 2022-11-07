from django import forms
from .models import Task

class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('user', 'title', 'description', 'task_date', 'task_hour',  'completed', )
        labels = {
            'user': 'User',
            'title': 'title',
            'description': 'description',
            'task_date': 'Date of task',
            'task_hour': 'Hour of task',
            'completed': 'is completed?',
        }