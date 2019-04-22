# Create your models here.
from django.db import models


class MovieList(models.Model):
    mname = models.TextField()
    content = models.TextField()
    data = models.DateField()
    actor = models.CharField(max_length=20)
    imgsrc = models.TextField()

    class Meta:
        managed = True
        db_table = 'movieList'


class GPU(models.Model):
    title = models.TextField()
    imgsrc = models.TextField()
    price = models.CharField(max_length=20)
    commentNum =models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'GPU'

