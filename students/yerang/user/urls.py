from django.urls import path

from user.views import SignUpView, LikedPostView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/<int:user_id>/likes', LikedPostView.as_view()),
]