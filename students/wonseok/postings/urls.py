from django.urls import path

from postings.views import CreateCommentView, CreatePostView, LikeCommentView, LikePostView, ReadCommentView, ReadPostView

urlpatterns = [
    path("/post/create", CreatePostView.as_view()),
    path("/post/read", ReadPostView.as_view()),
    path("/post/<int:post_id>/comment", ReadCommentView.as_view()),
    path("/post/<int:post_id>/comment/create", CreateCommentView.as_view()),
    path("/post/<int:post_id>/like", LikePostView.as_view()),
    path("/post/<int:post_id>/comment/like", LikeCommentView.as_view())
]