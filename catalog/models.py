from django.db import models

# Create your models here.
class Score(models.Model):
    name = models.CharField(max_length=255)
    scan = models.FileField()
    transcription = models.FileField()

class Comment(models.Model):
    contents = models.TextField()
    author = models.CharField(max_length=255)
    score = models.ForeignKey(Score, on_delete=models.CASCADE,
        related_name="comments")
