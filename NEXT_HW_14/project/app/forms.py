from django import forms
from django.contrib.auth.models import User
from .models import Comment

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'image']
