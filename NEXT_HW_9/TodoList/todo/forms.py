from django import forms
from .models import *

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'content', 'due_date']
        labels = {
            'name': '할 일 제목',
            'content': '할 일 내용', 
            'due_date': '기한',
        }