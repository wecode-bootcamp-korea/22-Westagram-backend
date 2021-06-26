from django.urls import path

from postings.views import CreateCommentView, CreatePostView, ReadPostView

urlpatterns = [
    path("/post/create", CreatePostView.as_view()),
    path("/post/read", ReadPostView.as_view()),
    path("/comment/create", CreateCommentView.as_view()),
]