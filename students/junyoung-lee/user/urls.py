from django import urls
from django.urls import path

from user.views import UserView

urlpatterns = [
    path('/signin', UserView.as_view()),
]
