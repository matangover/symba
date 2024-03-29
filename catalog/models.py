from django.db import models

class Score(models.Model):
    name = models.CharField(max_length=255)
    scan = models.FileField()
    transcription = models.FileField()

class Comment(models.Model):
    contents = models.TextField()
    author = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    score = models.ForeignKey(Score, on_delete=models.CASCADE,
        related_name="comments")
