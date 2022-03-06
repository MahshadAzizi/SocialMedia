from django import forms
from .models import Post, Comments


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['username', 'title', 'pic', 'description']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['username', 'comment']

