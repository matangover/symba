from django.db import models

# Create your models here.
class Score(models.Model):
    name = models.CharField(max_length=255)
    scan = models.FileField()
    transcription = models.FileField()
