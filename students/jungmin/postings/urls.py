from django.urls import path

from postings.views import CommentView, LikeView, PostingView


urlpatterns = [
    path('', PostingView.as_view()),
    path('/comment', CommentView.as_view()),
    path('/like', LikeView.as_view()),
]