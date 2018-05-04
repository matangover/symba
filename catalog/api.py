from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .models import Score, Comment
from .serializers import ScoreSerializer, CommentSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    def get_queryset(self):
        score = get_object_or_404(Score, pk=self.kwargs['score_id'])
        return score.comments
