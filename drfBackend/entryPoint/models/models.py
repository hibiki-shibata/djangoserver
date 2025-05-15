from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.core.exceptions import ValidationError



# Create your models here.
class AnswerAndKeywords(models.Model):
    keywords = ArrayField(
        models.CharField(max_length=50, blank=True, null=False),
                           db_index=True, 
                           null=False
                           )
    answer = models.CharField(max_length=100)
    timeStamp = models.TimeField()
    
    
    # This will validate the data handled around database, when clean method is called.
    def clean(self):
        for keyword in self.keywords:
            if not keyword.islower():
                raise ValidationError("Keyword must be lowercase.")


    # https://docs.djangoproject.com/en/5.2/ref/models/options/
    # class Meta:
    #     unique_together = ('keyword', 'user')