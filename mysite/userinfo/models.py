from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify

# Create your models here.
def custom_slugify(value):
    return default_slugify(value).lower()

class UserInfoModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="uploads/image/%Y/%m/%d", null=True)
    slug = AutoSlugField(populate_from='user', slugify=custom_slugify)

    def __str__(self):
        return self.user.username