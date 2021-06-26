from django.urls import path

from postings.views import CreateCommentView, CreatePostView, ReadCommentView, ReadPostView

urlpatterns = [
    path("/post/create", CreatePostView.as_view()),
    path("/post/read", ReadPostView.as_view()),
    path("/post/<int:post_id>/comment", ReadCommentView.as_view()),
    path("/post/<int:post_id>")
    path("/comment/create", CreateCommentView.as_view()),
]