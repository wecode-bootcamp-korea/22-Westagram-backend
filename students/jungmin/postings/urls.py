from django.urls import path

from postings.views import CommentView, LikeView, PostingView, RecommentView


urlpatterns = [
    path('', PostingView.as_view()),
    path('/comment', CommentView.as_view()),
    path('/like', LikeView.as_view()),
    path('/<int:post_id>', PostingView.as_view()),
    path('/comment/<int:comment_id>', CommentView.as_view()),
    path('/comment/recomment', RecommentView.as_view()),
]