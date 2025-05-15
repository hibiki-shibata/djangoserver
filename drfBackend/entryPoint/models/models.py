from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class AnswerAndKeywords(models.Model):
    keywords = ArrayField(models.CharField(max_length=50, blank=True, null=False), db_index=True, null=False)
    answer = models.CharField(max_length=100)
    timeStamp = models.TimeField()