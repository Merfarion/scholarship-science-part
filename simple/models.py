from django.db import models


class MySimpleModel(models.Model):
    col = models.CharField(max_length=10)