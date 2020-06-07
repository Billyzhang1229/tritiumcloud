from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model= models.PostsModel
        fields = ['title', 'picture', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentModel
        fields = ['content']

class CreateTagForm(forms.ModelForm):
    class Meta:
        model = models.TagModel
        fields = ['tagname', 'tagimage']