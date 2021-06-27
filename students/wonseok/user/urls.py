from django.urls import path

from user.views import FollowView, LoginView, SignupView

urlpatterns = [
    path("/signup", SignupView.as_view()),
    path("/login", LoginView.as_view()),
    path("/<int:user_id>/follow", FollowView.as_view())
]
