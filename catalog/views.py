from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Score
from .forms import CommentForm

def index(request):
    scores = Score.objects.all()
    context = {'scores': scores}
    return render(request, 'catalog/index.html', context)

def score(request, score_id):
    score = get_object_or_404(Score, pk=score_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.score = score
            comment_form.save()
            return HttpResponseRedirect('/score/%s/' % score_id)
    else:
        comment_form = CommentForm()

    comments = score.comments.order_by('-date')
    context = {'score': score, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'catalog/score.html', context)
