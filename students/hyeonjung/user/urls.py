from django.urls import path
from django.urls.resolvers import URLPattern

from .views import UserView

urlpatterns = [
    path('/signup', UserView.as_view()),
]