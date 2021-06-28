from django.urls import path
from postings.views import CreatePostsView

urlpatterns = [
    path('/post', CreatePostsView.as_view()),
]