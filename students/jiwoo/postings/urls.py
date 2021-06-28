from django.urls import path
from postings.views import CreatePostsView, CreateCommentsView

urlpatterns = [
    path('/post', CreatePostsView.as_view()),
    path('/comment', CreateCommentsView.as_view())
]