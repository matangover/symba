from django.contrib import admin

from .models import Score, Comment

class CommentInline(admin.StackedInline):
    model = Comment

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
