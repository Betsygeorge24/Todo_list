from django import forms
from .models import Task
from django.conf import settings

class TaskForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d-%m-%Y']  # Accept both formats
    )

    class Meta:
        model = Task
        fields = ['title', 'details', 'date', 'status']
