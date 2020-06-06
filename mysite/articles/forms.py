from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model= models.PostsModel
        fields = ['title', 'picture', 'content',]