from django.urls import path

from postings.views import CreateCommentView, CreatePostView, DeleteCommentView, DeletePostView, LikeCommentView, LikePostView, ReadCommentView, ReadPostView, UpdatePostView

urlpatterns = [
    path("/post/create", CreatePostView.as_view()),
    path("/post/read", ReadPostView.as_view()),
    path("/post/<int:post_id>/delete", DeletePostView.as_view()),
    path("/post/<int:post_id>/update", UpdatePostView.as_view()),
    path("/post/<int:post_id>/like", LikePostView.as_view()),
    path("/post/<int:post_id>/comment", ReadCommentView.as_view()),
    path("/post/<int:post_id>/comment/create", CreateCommentView.as_view()),
    path("/post/<int:post_id>/comment/like", LikeCommentView.as_view()),
    path("/post/<int:post_id>/comment/delete", DeleteCommentView.as_view()),
]