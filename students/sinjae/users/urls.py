from django.urls import path

from users.views import SignUp

urlpatterns = [
    path("/signup", SignUp.as_view()),
    path("/signin", SignUp.as_view()),
]
