from django.db import models
from django.conf import settings

# Create your models here.
class UserInfoModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="uploads/%Y/%m/%d/")
