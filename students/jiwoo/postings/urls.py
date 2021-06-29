from django.urls import path
from postings.views import CreatePostsView, CreateCommentsView, CreateLikesView

urlpatterns = [
    path('/post', CreatePostsView.as_view()),
    path('/comment', CreateCommentsView.as_view()),
    path('/like', CreateLikesView.as_view())
]