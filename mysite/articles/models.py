from django.db import models
from django.conf import settings
from autoslug import AutoSlugField

# Create your models here.
class TagModel(models.Model):
    tagname = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tagname

class PostsModel(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploadtime = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to="uploads/%Y/%m/%d/%H/%M")
    content = models.TextField()
    slug = AutoSlugField(populate_from='user')
    tags = models.ForeignKey(TagModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    content = models.CharField(max_length=255)
    commenttime = models.DateTimeField(auto_now_add=True)
    posts = models.ForeignKey(PostsModel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content