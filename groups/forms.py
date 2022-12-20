from django import forms
from .models import UsersGroup

class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = UsersGroup
        fields= ('name',)
