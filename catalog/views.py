from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Score

def index(request):
    scores = Score.objects.all()
    context = {'scores': scores}
    return render(request, 'catalog/index.html', context)

def score(request, score_id):
    score = get_object_or_404(Score, pk=score_id)
    context = {'score': score}
    return render(request, 'catalog/score.html', context)
