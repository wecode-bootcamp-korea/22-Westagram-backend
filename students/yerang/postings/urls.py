from postings.models import Post
from django.urls import path

from postings.views import PostView, CommentView

urlpatterns = [
    path('', PostView.as_view()),
    path('/create', PostView.as_view()),
    path('/<int:post_id>/comments', CommentView.as_view()),
]