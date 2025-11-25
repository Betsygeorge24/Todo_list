from django import forms
from .models import Task
from django.conf import settings
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d-%m-%Y']  # Accept both formats
    )

    class Meta:
        model = Task
        fields = ['title', 'details', 'date', 'status']


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
