from django.db import models


class MyProject(models.Model):
    status = models.TextField(max_length=200, verbose_name='Статус проекта', default=' ')
    place = models.IntegerField(verbose_name='Занятое место', default=0)