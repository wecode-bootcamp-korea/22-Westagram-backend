from django.urls import path
from users.views import SignupsView, SigninsView

urlpatterns = [
    path('/signup', SignupsView.as_view()),
    path('/signin', SigninsView.as_view())
]
