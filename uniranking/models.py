from django.db import models

# Create your models here.
class UniRegionModel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class RankingSystemModel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class UniversityModel(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(null=True)
    country = models.CharField(max_length=30, null=True)
    region = models.ForeignKey(UniRegionModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class UniRankingByYearModel(models.Model):
    university = models.ForeignKey(UniversityModel, on_delete=models.CASCADE)
    ranking_system = models.ForeignKey(RankingSystemModel, on_delete=models.CASCADE)
    rank_display = models.CharField(max_length=20)
    score = models.FloatField(null=True)
    year = models.IntegerField()

    def __str__(self):
        return self.university.title + ' ' + self.ranking_system.name+ ' ' +str(self.rank_display)