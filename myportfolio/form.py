from django import forms
from .models import *

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['name','email', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'name',
                'class': 'form-control',
                'placeholder': 'Steve Milner',
                'required': True,
                'data-error': 'Please enter your Name'
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'class': 'form-control',
                'placeholder': 'hello@websitename.com',
                'required': True,
                'data-error': 'Please enter your Email'
            }),
            'text': forms.Textarea(attrs={
                'id': 'text',
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write Your message',
                'required': True,
                'data-error': 'Please Write your Message'
            }),
        }