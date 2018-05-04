from django.urls import path, include
from rest_framework import routers

from . import views, api

router = routers.DefaultRouter()
router.register(r'scores', api.ScoreViewSet)
router.register(r'scores/(?P<score_id>[^/.]+)/comments', api.CommentViewSet, base_name='comments')

urlpatterns = [
    path('', views.index, name='index'),
    path('score/<int:score_id>/', views.score, name='score'),
    path('api/', include(router.urls)),
]
