from django.urls import path

from user.views import SigninView

urlpatterns = [
    path('/signin', SigninView.as_view()),
]