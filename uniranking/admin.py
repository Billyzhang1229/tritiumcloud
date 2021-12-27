from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UniRegionModel)
admin.site.register(models.RankingSystemModel)
admin.site.register(models.UniversityModel)
admin.site.register(models.UniRankingByYearModel)
