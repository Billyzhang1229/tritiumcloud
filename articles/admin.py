from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.PostsModel)
admin.site.register(models.TagModel)
admin.site.register(models.CommentModel)
admin.site.register(models.ArticleViewsModel)