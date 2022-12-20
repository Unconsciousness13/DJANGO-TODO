from django import forms
from .models import Task
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'


class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'task_date', 'task_hour',  'completed', )
        labels = {
            'title': 'Title',
            'description': 'Description',
            'task_date': 'Date of task',
            'task_hour': 'Hour of task',
            'completed': 'Completed',
        }
        widgets = {
            'task_date': DateInput(),
            'task_hour': forms.TextInput(attrs={'type':'time'}),
        }
 

class AddTaskBg(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'task_date', 'task_hour',  'completed', )
        labels = {
            'title': 'Заглавие',
            'description': 'Описание',
            'task_date': 'Дата на задача',
            'task_hour': 'Час на задача',
            'completed': 'Завършена',
        }
        widgets = {
            'task_date': DateInput(),
            'task_hour': forms.TextInput(attrs={'type':'time'}),
        }
 

class AddTaskEs(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'task_date', 'task_hour',  'completed', )
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'task_date': 'Fecha de la tarea',
            'task_hour': 'Hora de la tarea',
            'completed': 'Terminada',
        }
        widgets = {
            'task_date': DateInput(),
            'task_hour': forms.TextInput(attrs={'type':'time'}),
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('user_name',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',)
        
        
class RegisterFormEs(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('user_name',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',)
        labels = {'user_name': 'Usuario',
                  'first_name': 'Nombre',
                  'last_name': 'Apellido',
                  'email': 'Correo electronico',
                  'password1': 'Contraseña',
                  'password2': 'Confirmar Contraseña'}
        
class RegisterFormBg(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('user_name',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',)
        
        labels = {'user_name': 'Потребителско име',
                  'first_name': 'Име',
                  'last_name': 'Фамилия',
                  'email': 'Електронна поща',
                  'password1': 'Парола',
                  'password2': 'Потвърди парола'}


class UpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('user_name',
                  'first_name',
                  'last_name',
                  'email',
                  )
        
