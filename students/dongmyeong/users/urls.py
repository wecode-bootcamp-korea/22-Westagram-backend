from django.urls import path

from users.views import FollowView, SigninView, SignupView

urlpatterns = [
    path('/signup'                   , SignupView.as_view()),
    path('/signin'                   , SigninView.as_view()),
    path('/follow'                   , FollowView.as_view()),
    path('/follow/<int:followee_id>' , FollowView.as_view()),
]
