from posts.views import PostView
from django.urls import path

urlpatterns = [
    path("/posting", PostView.as_view()),
]
