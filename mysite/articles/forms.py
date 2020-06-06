from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='title', max_length=50)
    picture = forms.ImageField(label='picture', upload_to="uploads/%Y/%m/%d/")
    content = forms.TextField(label='content')