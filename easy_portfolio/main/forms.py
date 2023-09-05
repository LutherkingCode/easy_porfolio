from django import forms
from django.contrib.auth.models import User
from .models import Project
from django.contrib.auth.forms import UserCreationForm

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'category']
    




