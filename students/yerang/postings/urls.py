from user.models import Like
from postings.models import Post
from django.urls import path

from postings.views import PostView, CommentView, LikeView

urlpatterns = [
    path('', PostView.as_view()),
    path('/create', PostView.as_view()),
    path('/<int:post_id>/comments', CommentView.as_view()),
    path('/<int:post_id>/likes/<int:user_id>', LikeView.as_view()),
    path('/<int:post_id>/likes', LikeView.as_view()),
]