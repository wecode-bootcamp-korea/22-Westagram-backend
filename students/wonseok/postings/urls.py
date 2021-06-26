from django.urls import path

from postings.views import CreatePostView, ReadPostView

urlpatterns = [
    path("/post/create", CreatePostView.as_view()),
    path("/post/read", ReadPostView.as_view()),
]