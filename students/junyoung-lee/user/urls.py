from django import urls
from django.urls import path

from user.views import SignupView

urlpatterns = [
    path('/signup', SignupView.as_view()),
]
