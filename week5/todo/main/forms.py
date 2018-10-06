from django import forms
from .models import Task, List
from django.contrib.auth.models import User

class SearchListForm(forms.Form):
    name = forms.CharField(max_length=100)

class TaskForm(forms.Form):
    name = forms.CharField(max_length = 255)
    due_on = forms.DateTimeField()
    owner = forms.ModelChoiceField(queryset=User.objects.all())

class UpdateTaskForm(forms.Form):
    name = forms.CharField(max_length = 255)
    due_on = forms.DateTimeField()
    
class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('name',)